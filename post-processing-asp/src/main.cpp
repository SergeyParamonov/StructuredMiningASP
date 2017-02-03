#include "miners.cpp"
#include "asp_engine.cpp"
#include "experiment.cpp"
#include <ctime>



int main(int argc, char *argv[]){
  string type = "itemset";
  vector<string> datasets {"mushroom.txt", "primary-tumor.txt", "soybean.txt", "splice-1.txt","tic-tac-toe.txt","vote.txt","zoo.txt"};
  vector<string> pattern_types = {"closed", "maximal", "skyline"};
  ofstream stats_file;
  stats_file.open("itemset_runtimes.txt");
  for(string const dataset: datasets){  
    string full_path_to_dataset = "datasets/itemsets/" + dataset;
    stats_file << "dataset: " << dataset << "\n";  
    for(string const pattern_type : pattern_types){
      stats_file << pattern_type + "\n";
      unique_ptr<Experiment> e = make_unique<Experiment>(type);   
      auto times = e->run_time_in_range(full_path_to_dataset, 35, 40, 5, pattern_type);
      for (auto const& pair : times){
        stats_file << "threshold: " + to_string(pair.first) + " time: " + to_string(pair.second) +"\n"; 
      }
    }
  }
  stats_file.close();
  return 0;
}
