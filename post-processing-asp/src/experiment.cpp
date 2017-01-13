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

  void run_experiment(string dataset, int threshold, string pattern_type){
    miner->run_solver(dataset, tmp_file,threshold);
    vector<unique_ptr<Pattern>> patterns = miner->parse_solver_output(tmp_file);
    miner->write_asp_patterns_to_file(move(patterns), dataset_file);
    patterns.clear();
    asp_engine->run_on_file(dataset_file, output_filename, pattern_type);
  
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
