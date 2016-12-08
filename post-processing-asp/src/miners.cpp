
#include <iostream>
#include <stdlib.h>

using namespace std;

class Miner{
 public:
   virtual void run_solver(){}
   virtual ~Miner(){}
};

class ItemsetMiner : public Miner{
  public:
    ItemsetMiner(){};
    ~ItemsetMiner(){};
    void run_solver(){
      string miner_name = "bin/eclat";
      string dataset_name = "datasets/itemsets/mushrooms.dat";
      string output = "tmp/tmp_output";
      string command = miner_name + " " + dataset_name +" -o " + output + "\n";
      cout << "executing the command " << command;
      system(command.c_str());
    }
};
