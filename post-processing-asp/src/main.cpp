#include "miners.cpp"


int main(){
  string tmp_file ="tmp/tmp_output";
  Miner *miner = pick_miner("itemset");
  miner->run_solver("datasets/itemsets/mushrooms.dat",tmp_file);
  list<unique_ptr<Pattern>> *patterns = miner->parse_solver_output(tmp_file);
  patterns->clear();
  return 0;
}
