#include "miners.cpp"


int main(){
    string tmp_file ="tmp/tmp_output";
    unique_ptr<Miner> miner = pick_miner("itemset");
    miner->run_solver("datasets/itemsets/mushrooms.dat",tmp_file);
    vector<unique_ptr<Pattern>> patterns = miner->parse_solver_output(tmp_file);
    for (auto &p: patterns){
     cout << p->to_string() << "test" << endl; 
     for (auto i: p->get_items()){
      cout << i << " ";
     }
     cout << endl;
    ; 
    }
    patterns.clear();
    return 0;
}
