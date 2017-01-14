#include "miners.cpp"
#include "asp_engine.cpp"
#include "experiment.cpp"
#include <ctime>



int main(int argc, char *argv[]){
    string type = "itemset";
    string input_dataset = "datasets/itemsets/mushroom.txt";
    string pattern_type = "closed";
    unique_ptr<Experiment> e = make_unique<Experiment>(type);   
    auto times = e->run_time_in_range(input_dataset, 30, 40, 1, pattern_type);
    for (auto const& pair : times){
      cout << "threshold :" + to_string(pair.first) + " time: " + to_string(pair.second) +"\n"; 
    }

//  clock_t start_time = clock();
//  int threshold = 20;
//  miner->run_solver("datasets/itemsets/mushroom.txt",tmp_file,threshold);
//  vector<unique_ptr<Pattern>> patterns = miner->parse_solver_output(tmp_file);
//  miner->write_asp_patterns_to_file(move(patterns), dataset_file);
//  patterns.clear();
//  unique_ptr<ASP_Engine> asp_engine = make_unique<ASP_Engine>();
//  asp_engine->run_on_file(dataset_file, output_filename);
//  clock_t end_time = clock();
//  cout << "overall time " + to_string(double(end_time - start_time)/CLOCKS_PER_SEC) + "\n";
    return 0;
}
