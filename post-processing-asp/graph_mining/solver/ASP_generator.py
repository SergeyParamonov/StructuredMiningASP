from __future__ import print_function
import os
from pudb import set_trace as bp
from tqdm import tqdm

class ASP_processor():

  def __init__(self):
    pass

  def process(self, patterns, pattern_type):
    dominated_set = []
    output_patterns = []
    for i, pattern in tqdm(enumerate(patterns),total=len(patterns)):
      self.generate_code_selected_graph(pattern)
      self.generate_dataset(i, patterns, dominated_set)
      self.execute_solver(pattern_type)
      is_condensed = self.analyze_output()
      if is_condensed:
        output_patterns.append(pattern)
      else:
        dominated_set.append(i) # not a solutions
    return output_patterns
      


  def generate_dataset(self, selected_id, patterns, dominated_set):
    with open('tmp/dataset_graph',"w") as dataset_file:
      for index, graph in enumerate(patterns):
        if index not in dominated_set and index != selected_id:
            self.generate_graph(graph, index, dataset_file)

  def generate_graph(self, graph, index, dataset_file):
     print('graph({}).'.format(index), file=dataset_file)
     print('support({gid},{frequency}).'.format(gid=index,frequency=graph.get_support()),file=dataset_file)

     for edge, label in graph.edges.items():
         v1,v2 = edge
         print('edge({index},{v1},{v2},{label}).'.format(v1=v1,v2=v2,label=label,index=index), file=dataset_file)
         print('edge({index},{v2},{v2},{label}).'.format(v1=v1,v2=v2,label=label,index=index), file=dataset_file)
     for vertex, label in graph.nodes.items():
         print('node({index},{vertex},{label}).'.format(vertex=vertex,label=label,index=index), file=dataset_file)
     
      
  def execute_solver(self, pattern_type):
     if pattern_type == "closed":
         os.system('clingo asp_encoding/closed tmp/selected_graph tmp/dataset_graph > tmp/decision')
     if pattern_type == "maximal":
         os.system('clingo asp_encoding/maximal tmp/selected_graph tmp/dataset_graph > tmp/decision')


  def analyze_output(self):
    with open('tmp/decision','r') as clingo_output:
      data = clingo_output.read()
    if "UNSATISFIABLE" in data:
      return True
    else:
      return False

  def generate_code_selected_graph(self, graph):
    with open('tmp/selected_graph',"w") as selected_file:
      print('selected_sup({}).'.format(graph.get_support()),file=selected_file)
      for edge, label in graph.edges.items():
        v1,v2 = edge
        print('selected_edge({v1},{v2},{label}).'.format(v1=v1,v2=v2,label=label), file=selected_file)
        print('selected_edge({v2},{v2},{label}).'.format(v1=v1,v2=v2,label=label), file=selected_file)
      for vertex, label in graph.nodes.items():
        print('selected_node({vertex},{label}).'.format(vertex=vertex, label=label), file=selected_file)



