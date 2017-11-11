import os, sys
import csv
import collections
from solver.Constraint import LengthConstraint, IfThenConstraint, CostConstraint
from wrapper import fpMining_pure, fpMining_postpro


def main():
    typeList = ['graph']
    graph_supports    = [0.4, 0.35, 0.3, 0.25, 0.20,]
    nctrer_supports   = [0.4, 0.35, 0.3, 0.25, 0.20,]
    compound_supports = [0.4, 0.35, 0.3, 0.25, 0.20,]

    params = dict()
    params['type'] = 'graph'
    #TODO do the same for seq and graphs
    support = {("graph", 'Compound_422')           : compound_supports,
                ("graph", 'nctrer.gsp')             : nctrer_supports,
                ("graph", 'yoshida.gsp')            : graph_supports,
                ("graph", 'bloodbarr.gsp')          : graph_supports
                }
    dominances = ['closed', 'maximal']
    graph_datasets = ['nctrer.gsp','yoshida.gsp', 'bloodbarr.gsp']
    datasets = {
        'graph'    : graph_datasets
    }
    exp_path = 'output/'
    for dominance in dominances:
        params['type'] = 'graph'
        for dataset in datasets['graph']:
            results = []
            params['data'] = dataset
            params['output'] = dataset.split('.')[0]+'.output'
            params['dominance'] = dominance
            supps = support[('graph', dataset)]
            for s in supps:
                params['support'] = s
                params['data'] = dataset
                params['output'] = dataset.split('.')[0]+'.output'
                _, num_patterns, timecost_pure = fpMining_pure(params)
                _, num_patterns, num_final_patterns, step1_tc, step3_tc = fpMining_postpro(params)
                results.append((s, '{0:.4f}'.format(timecost_pure),
                                '{0:.4f}'.format(step1_tc+step3_tc),
                                '{0:.4f}'.format(step1_tc),
                                '{0:.4f}'.format(step3_tc),
                                '{0}'.format(num_patterns),
                                '{0}'.format(num_final_patterns)
                                ))
            with open('{path}/{dominance}/{type}/{dataset}.csv'.format(path=exp_path, dominance=params['dominance'], type=t, dataset=dataset.split('.')[0]), 'wb') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['freq', 'specialised', 'postpro', 'step1',  'step3', 'num_of_freq_patterns', 'num_of_final_patterns'])
                writer.writerows(results)



      
if __name__ == '__main__':
  main()
