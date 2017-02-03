#include <fstream>
#include <stdlib.h>
#include "pattern.cpp"
#include <memory>
#include <vector>

using namespace std;


class Miner{
  public:
    virtual void run_solver(string dataset_name, string outputfile, int threshold){}
    virtual vector<shared_ptr<Pattern>> parse_solver_output(string filepath){}
    virtual ~Miner(){}

    void write_asp_patterns_to_file(vector<shared_ptr<Pattern>> patterns, string outputfilename){
      cout << "writing ASP data to the file: " << outputfilename << "\n"; 
      ofstream myfile;
      myfile.open(outputfilename);
      for (auto &p: patterns){
        myfile << p->make_ASP_str();
      }
      myfile.close();
    }

};

class ItemsetMiner : public Miner{
  public:
    ItemsetMiner(){};
    ~ItemsetMiner(){};

    void run_solver(string dataset_name, string outputfile, int threshold){
      string miner_name = "bin/eclat -v ':%a' -s" + to_string(threshold);
      string command = miner_name + " " + dataset_name +" -o " + outputfile + " 2> tmp/fnull " + " \n";
      cout << "executing the command " << command;
      system(command.c_str());
    };

    vector<shared_ptr<Pattern>> parse_solver_output(string filepath){
      string line;
      ifstream f (filepath);
      vector<shared_ptr<Pattern>> v;
      while(getline(f, line)) {
        v.push_back(make_shared<Itemset>(line));
      }
      return move(v);
    };

};

unique_ptr<Miner> pick_miner(string datatype){
  if(datatype == "itemset"){
    return make_unique<ItemsetMiner>();
  }
};


