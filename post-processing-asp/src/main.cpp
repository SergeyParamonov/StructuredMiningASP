#include <iostream>
#include <stdlib.h>

using namespace std;

int main(){
  string miner_name = "bin/eclat";
  string dataset_name = "datasets/itemsets/mushooms.dat";
  string output = "tmp/tmp_output";
  string command = miner_name + " " + dataset_name +" > " + output + "\n";
  cout << "executing the command " << command;
  system(command.c_str());
  return 0;
}
