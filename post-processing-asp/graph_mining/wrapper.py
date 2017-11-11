from pudb import set_trace as bp
import getopt, time
import ConfigParser
import collections

from solver.method import *
from solver.utils import logger
from solver.Constraint import LengthConstraint, IfThenConstraint, CostConstraint, process_constraints
from solver.ASP_generator import ASP_processor

default_parameters = 'config.ini'


# Debug print
def DebugPrint(s):
    print s

with open("tmp/sergey_tmp_log","w"): # clean the log file before each run
    pass

def sergeylog(s): #dump info into the log file
    with open("tmp/sergey_tmp_log","a") as logfile:
        logfile.write(s)


@logger
def fpMining_pure(inputs):
    if inputs['type']   == 'graph':
        inputs['data']   = 'data/gSpan/' + inputs['data']
        inputs['output'] = 'output/gSpan/' + inputs['output']
        method = gSpan(inputs)
    else:
        print 'Does not support "type == %s"!' % inputs['type']
        sys.exit(2)

    start1   = time.time()
    output   = method.mining()
    patterns = method.parser(output)
    end1     = time.time()
    print "\n*************************************"
    print 'Number of frequent patterns with constraints (pure exec): %s' % len(patterns)

    return patterns, len(patterns), end1-start1


@logger
def fpMining_postpro(inputs):
    if inputs['type'] == 'graph':
        if 'data/' not in inputs['data']:
            inputs['data']   = 'data/gSpan/' + inputs['data']
            inputs['output'] = 'output/gSpan/' + inputs['output']
        method = gSpan(inputs)
    else:
        print 'Does not support "type == %s"!' % inputs['type']
        sys.exit(2)

    params = inputs

    # step 1 time cost
    start1   = time.time()
    output   = method.mining()
    patterns = method.parser(output)
    end1     = time.time()
    print "# of patterns", len(patterns)

    # step 3 time cost
    start3   = time.time()
    final_patterns = dominance_check(params, patterns)
    if final_patterns:
        final_patterns = list(final_patterns)
    else: final_patterns = []
    print "# of dominance patterns", len(final_patterns)
    end3 = time.time()
 
    print "step1: {}, step2: {}".format(end1-start1, end3-start3)
    return final_patterns, len(patterns), len(final_patterns), end1-start1, end3-start3



def dominance_check(params, patterns):
    pattern_type = params['dominance'] # closed, maximal
    asp_processor   = ASP_processor()
    output_patterns = asp_processor.process(patterns, pattern_type)
    return output_patterns


if __name__ == "__main__":
    # deal with command parameters
    if len(sys.argv) < 2:
        print 'Needs input file\n<wrapper.py -h> for help!'
        sys.exit(2)

    config_file = default_parameters        # config file path
    specialised = False
    params = {}     # Dict to store input parameters

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hc:s:', ['help=', 'config='])
    except getopt.GetoptError:
        print('wrapper.py -c <configfile> -s <True or False>\nSet input data and output file in config file')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'wrapper.py -c <configfile> -i <inputfile> -o <outputfile>'
            sys.exit(2)
        elif opt in ('-c', '--config'):
            config_file = arg
        elif opt in ('-s', '--specialised'):
            if arg in ('true', 'True', 'T'):
                specialised = True

    # read parameters from config file
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    sections = config.sections()

    # read basic parameters
    section = 'Parameters'
    options = config.options(section)
    for option in options:
        try:
            params[option] = config.get(section, option)
            if params[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            params[option] = None
    print('Parameters: %s' % params)
   
    # read constraints
    section = 'Constraints'
    options = config.options(section)
    params['constraints'] = dict()
    for option in options:
        if option == 'length':
            max_len = int (config.get(section, option))
            params['constraints']['length'] = LengthConstraint(max_len)
        elif option == 'ifthen':
            pre, post = config.get(section, option).split(';')
            params['constraints']['ifthen'] = IfThenConstraint(int(pre), int(post))
        elif option == 'cost':
            cost_mapping = collections.defaultdict(int)
            costs = config.get(section, option).split(';')
            costs, max_cost = costs[:-1], costs[-1].split(':')[-1]
            for c in costs:
                id, cost = c.split(':')
                cost_mapping[int(id)] = int(cost)
            params['constraints']['cost'] = CostConstraint(int(max_cost), cost_mapping)
        else:
            print("Does not support this type of constraint: %s" % option)


    # frequent pattern mining
    if specialised:
        patterns, _, time_pure = fpMining_pure(params)
    #for i in range(10):
    #    print patterns[i].get_graphx().nodes(data=False)
    final_patterns, _1, _2, time_step1, time_step2 = fpMining_postpro(params)
