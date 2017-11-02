#include <stdlib.h>

class ASP_Engine{
  public:
    ASP_Engine(){};
   ~ASP_Engine(){};


  void run_on_file(string data_filename, string output_filename, string pattern_type, string data_type){
    string program;
    bool is_testing_under_constraints = false;
    if (is_testing_under_constraints){
      program = "asp_encodings/"+data_type+"_"+pattern_type+"_under_constraints.asp";
    }
    else{
      program = "asp_encodings/"+data_type+"_"+pattern_type+".asp";
    }
    string command = "clingo " + program + " " + data_filename + " 0 > " + output_filename;     
    cout << "executing... " + command + "\n";
    system(command.c_str());
  }
};
