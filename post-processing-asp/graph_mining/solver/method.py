import os, sys
import platform
import subprocess
from tqdm import tqdm
from Pattern import *

# ----------------------------------------------------------
# gSpan command:
# ./gSpan -file [file_name] -support [support: float] &> log
# ----------------------------------------------------------

class Mining(object):
    """Abstract class"""

    def __init__(self, inputs):
        # example: inputs{'type': 'itemset', 'matching': 'exact', 'constraints': 'frequency', 'dominance': 'max'}
        self.type = inputs['type']
        if 'matching' in inputs:
            self.matching = inputs['matching']
        else:
            self.matching = None
        if 'constraint' in inputs:
            self.constraint = inputs['constraint']
        else:
            self.constraint = None
        if 'dominance' in inputs:
            self.dominance = inputs['dominance']
        else:
            self.dominance = None
        if 'support' in inputs:
            self.support = float(inputs['support'])
        else:
            self.support = 0.1
        if 'data' in inputs:
            self.data = inputs['data']
        else:
            print 'Need input data file!'
            sys.exit(2)
        if 'output' in inputs:
            self.output = inputs['output']
        else:
            self.output = "-"
        self.patternSet = None

    def mining(self):
        pass

    def parser(self):
        pass


class gSpan(Mining):
    """Use gSpan to mining frequent subgraphs"""


    def __init__(self, inputs):
        Mining.__init__(self, inputs)
        Pattern.id2pattern = {}

    def mining(self):
        gSpan_exec = ''
        if platform.system() == "Linux":
            # gSpan = "./exec/gspan"
            gSpan_exec = "./exec/gspan-CT"
        else:
            gSpan_exec = "./exec/gspan"
        options = ''
        if self.support:
            options = ''.join('-support %s' % self.support)

        #child = subprocess.Popen([gSpan, "-f", self.data, "-s", self.support, "-o -i"], stdout=subprocess.PIPE)
        # child = subprocess.Popen([gSpan_exec, "-file", self.data, "-output", self.output, options], shell=False, stderr=devnull)
        command = '{exe} -file {data} -output {output} -support {support} 1> tmp/FNULL'.format(exe=gSpan_exec, data=self.data, output=self.output, support=self.support)
        with open(self.output,"w") as outputfile:
            print(command) #cleaning output
        os.system(command)

        with open(self.output, 'r') as fout:
          print(self.output)
          result = fout.read()

        return result

    def parser(self, stdOutput, path=None):
        self.patternSet = self.parserGraph(stdOutput)
        return self.patternSet

    def parserGraph(self, stdOutput, path=None):
        if path:
            fg = open(path, 'r')
            stdOutput = fg.readlines()
            fg.close()
        return [graph for graph in self.parse_gspan_output(stdOutput)]

    def parse_gspan_output(self, stdOutput):
        data = stdOutput.split('t #')
        for graph_txt in data:
            graph = self.parse_gspan_graph(graph_txt)
            if graph:
                yield graph

    def parse_gspan_graph(self, text):
        if '*' not in text:
            return None
        graph = Graph()
        for line in text.splitlines():
            if '*' in line:
                graph_id, support = line.split('*')
                graph_id = int(graph_id)
                graph.set_id(graph_id)
                Graph.id2pattern[graph_id] = graph
                graph.set_support(int(support))
            if 'parent' in line:
                _, parent_id = line.split(':')
                graph.set_parent(int(parent_id))
            if 'v ' in line:
                _, node_id, node_label = line.split()
                graph.add_node(int(node_id), node_label)
            if 'e ' in line:
                _, edge_from, edge_to, label = line.split()
                graph.add_edge(int(edge_from), int(edge_to), label)
            if 'x ' in line:
                transactions = line.split()
                coverage = set()
                for t in transactions:
                    if 'x' not in t and t != '':
                        coverage.add(int(t))
                graph.build_coverage(coverage)
        graph.set_stats_and_mapping()
        return graph

    def getPatterns(self):
        return self.patternSet


