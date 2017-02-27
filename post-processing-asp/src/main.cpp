#include "pattern.cpp"
#include "miners.cpp"
#include "asp_engine.cpp"
#include "experiment.cpp"
#include <ctime>



int main(int argc, char *argv[]){
  string type = "itemset";
// vector<string> datasets {"mushroom.txt", "primary-tumor.txt", "soybean.txt", "splice-1.txt","tic-tac-toe.txt","vote.txt","zoo.txt"};
//string type = "sequence";
/*vector<pair<string,int> > datasets { 
                                       make_pair("iprg.dat",5),
                               //      make_pair("asp_200.dat",5),
                               //      make_pair("asp_300.dat",5), 
 //                                     make_pair("asp_default.dat",5),
                                      make_pair("unix_users.dat",5),
                                       make_pair("jmlr.dat",6)
                                     }; */
  vector<pair<string,int> > datasets { 
                                        make_pair("mushroom.txt",22),
                                        make_pair("vote.txt",22)
                                     }; 

  vector<string> pattern_types = {"closed"};//,"maximal","skyline"};
  ofstream stats_file;
  for(const pair<string,int> dataset_freq_pair: datasets){  
    string dataset = dataset_freq_pair.first;
    int min_freq = dataset_freq_pair.second;
    string full_path_to_dataset = "datasets/" + type + "/" + dataset;
    string stats_files_name = "results/"+dataset+"_"+type+"_runtimes.txt";
    stats_file.open(stats_files_name.c_str());
    stats_file << "pattern_type,threshold,time,num_of_patterns\n"; 
    for(string const pattern_type : pattern_types){
      unique_ptr<Experiment> e = make_unique<Experiment>(type);   
      cout << "global id " << to_string(Sequence::global_id) << "\n";
      auto times = e->run_time_in_range(full_path_to_dataset, min_freq, 30, 1, pattern_type);
      for (auto const& pair_of_pairs : times){
        float frequency = pair_of_pairs.first;
        int time = pair_of_pairs.second.first;
        int num_of_patterns = pair_of_pairs.second.second;
        stats_file << pattern_type+","+to_string(frequency)+","+to_string(time)+","+to_string(num_of_patterns)+"\n"; 
        stats_file.flush();
      }
    }
  stats_file.close();
  }
  return 0;
}
