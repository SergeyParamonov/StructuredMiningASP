#include "pattern.cpp"
#include "miners.cpp"
#include "asp_engine.cpp"
#include "experiment.cpp"
#include <ctime>



int main(int argc, char *argv[]){
//  string type = "itemset";
// vector<string> datasets {"mushroom.txt", "primary-tumor.txt", "soybean.txt", "splice-1.txt","tic-tac-toe.txt","vote.txt","zoo.txt"};
  string type = "sequence";
  vector<string> datasets {"jmlr.dat", "unix_users.dat"};
  vector<string> pattern_types = {"closed", "maximal", "skyline"};
  ofstream stats_file;
  string stats_files_name = type+"_runtimes.txt";
  stats_file.open(stats_files_name.c_str());
  for(string const dataset: datasets){  
    string full_path_to_dataset = "datasets/" + type + "/" + dataset;
    stats_file << "dataset: " << dataset << "\n";  
    for(string const pattern_type : pattern_types){
      stats_file << pattern_type + "\n";
      unique_ptr<Experiment> e = make_unique<Experiment>(type);   
      cout << "global id " << to_string(Sequence::global_id) << "\n";
      auto times = e->run_time_in_range(full_path_to_dataset, 40, 45, 5, pattern_type);
      for (auto const& pair : times){
        stats_file << "threshold: " + to_string(pair.first) + " time: " + to_string(pair.second) +"\n"; 
      }
    }
  }
  stats_file.close();
  return 0;
}
