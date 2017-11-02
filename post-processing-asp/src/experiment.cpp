#include <map>

class Experiment{
  public:
    Experiment(){};
    ~Experiment(){};

    Experiment(string type){

      this->type = type;
      tmp_file =(boost::format("tmp/%1%_tmp_output") % global_id).str();
      dataset_file = (boost::format("processed/%1%_patterns") % global_id).str();
      output_filename = (boost::format("tmp/%1%_patterns_asp_output") % global_id).str();
      miner = pick_miner(type);
      global_id += 1;
      asp_engine = make_unique<ASP_Engine>();
    }

  int run_experiment(string dataset, int threshold, string pattern_type){
    
    int number_of_patterns = -1;
    Itemset::global_id = 1;
    Sequence::global_id = 1;
    miner->run_solver(dataset, tmp_file,threshold);
    vector<shared_ptr<Pattern>> patterns = miner->parse_solver_output(tmp_file);
    number_of_patterns = patterns.size();
    miner->write_asp_patterns_to_file(patterns, dataset_file);
    asp_engine->run_on_file(dataset_file, output_filename, pattern_type, this->type);
    patterns.clear();
    return number_of_patterns;
  }

  int get_str_dif(time_t start_time, time_t end_time){
    return int(end_time - start_time);
  }

  pair<int, int> run_timed_experiment(string dataset, int threshold, string pattern_type){
    time_t start_time = time(NULL);
    int number_of_patterns = run_experiment(dataset, threshold, pattern_type);
    time_t end_time  = time(NULL);
    int overall_time = get_str_dif(start_time,end_time);
    cout << "overall time " + to_string(overall_time) + "\n";
    return pair<int,int>(overall_time,number_of_patterns);
  }

  std::map <float,pair<int,int> > run_time_in_range(string dataset, float start_threshold, float end_threshold, float step, string pattern_type){
    map<float, pair<int,int> > times;
    for(float i = end_threshold; i >= start_threshold; i -= step){
      times[i] = run_timed_experiment(dataset, i, pattern_type);
    }
    return times;
  }

  string get_dataset_file(){
    return dataset_file;
  }

  private:
    string type;
    static int global_id;
    unique_ptr<Miner>miner;
    string tmp_file;
    string dataset_file;
    string output_filename;
    unique_ptr<ASP_Engine> asp_engine;
};

int Experiment::global_id = 1;
