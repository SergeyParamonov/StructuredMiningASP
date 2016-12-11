#include "miners.cpp"


int main(){
    string tmp_file ="tmp/tmp_output";
    unique_ptr<Miner> miner = pick_miner("itemset");
    miner->run_solver("datasets/itemsets/mushrooms.dat",tmp_file);
    vector<unique_ptr<Pattern>> patterns = miner->parse_solver_output(tmp_file);
    miner->write_asp_patterns_to_file(move(patterns), "tmp/test_asp_data");
    patterns.clear();
    return 0;
}
