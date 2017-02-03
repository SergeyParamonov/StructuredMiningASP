#include <stdlib.h>

class ASP_Engine{
  public:
    ASP_Engine(){};
   ~ASP_Engine(){};
/*
   void run_with_selected_on_file(const vector<shared_ptr<Pattern>> patterns, string data_filename, string output_filename, string pattern_type){
    string program;
    if (pattern_type == "closed"){
      program = "asp_encodings/with_selected_closed.asp";
    }

    ofstream selected_file;
    string tmp_selected_filename = "tmp/selected";
    for (auto &p: patterns){
      selected_file.open(tmp_selected_filename, ofstream::out | ofstream::trunc);
      string selected_repr = p->make_selected_ASP_repr();
      cout << selected_repr + "\n";
      selected_file << selected_repr;
      selected_file.close();
      string command = "clingo -q " + program + " " + data_filename + " " + tmp_selected_filename + " &> " + output_filename;     
      cout << "executing... " + command + "\n";
      system(command.c_str());
    }
  }*/

  void run_on_file(string data_filename, string output_filename, string pattern_type){
    string program;
    if (pattern_type == "closed"){
      program = "asp_encodings/closed_post_processing.asp";
    }
    else if(pattern_type == "maximal"){
      program = "asp_encodings/maximal_post_processing.asp";
    }
    else if(pattern_type == "skyline"){
      program = "asp_encodings/skyline.asp";

    }
    string command = "clingo " + program + " " + data_filename + " 0 > " + output_filename;     
    cout << "executing... " + command + "\n";
    system(command.c_str());
  }
};
