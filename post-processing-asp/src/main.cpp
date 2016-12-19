#include "miners.cpp"


int main(int argc, char *argv[]){
    
    string tmp_file ="tmp/tmp_output";
    unique_ptr<Miner> miner = pick_miner("itemset");
    miner->run_solver("datasets/itemsets/mushroom.txt",tmp_file);
    vector<unique_ptr<Pattern>> patterns = miner->parse_solver_output(tmp_file);
    miner->write_asp_patterns_to_file(move(patterns), "processed/mushroom_patterns");
    patterns.clear();
    return 0;
}
