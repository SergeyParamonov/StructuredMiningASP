class Experiment{
  string type;
  int global_id;
  public:
    Experiment(){};
    ~Experiment(){};

    Experiment(string type){
      this.type = type;
      string tmp_file =(boost::format("tmp/%1%_tmp_output") % global_id).str();
      string dataset_file = "processed/%1%_patterns";
      string output_filename = "tmp/patterns_asp_output";
      unique_ptr<Miner> miner = pick_miner("itemset");
      global_id += 1;
    }

};
int Experiment::global_id = 1;
