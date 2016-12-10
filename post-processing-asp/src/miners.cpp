#include <iostream>
#include <fstream>
#include <stdlib.h>
#include "pattern.cpp"
#include <list>
#include <memory>



using namespace std;


class Miner{
 public:
   virtual void run_solver(string dataset_name, string outputfile){}
   virtual list<unique_ptr<Pattern>>* parse_solver_output(string filepath){}
   virtual ~Miner(){}
};

class ItemsetMiner : public Miner{
  public:
    ItemsetMiner(){};
    ~ItemsetMiner(){};
    void run_solver(string dataset_name, string outputfile){
      string miner_name = "bin/eclat -v ' (%a)'";
      string command = miner_name + " " + dataset_name +" -o " + outputfile + "\n";
      cout << "executing the command " << command;
      system(command.c_str());
    };

    list<unique_ptr<Pattern>>* parse_solver_output(string filepath){
      string line;
      ifstream f (filepath);
      list<unique_ptr<Pattern>> *v = new list<unique_ptr<Pattern>>();
      while(getline(f, line)) {
        v->push_back(make_unique<Itemset>(line));
      }
      return v;
    };
    
};

Miner* pick_miner(string datatype){
  if(datatype == "itemset"){
    return new ItemsetMiner();
  }
};


