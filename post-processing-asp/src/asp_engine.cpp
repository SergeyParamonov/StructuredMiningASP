#include <stdlib.h>

class ASP_Engine{
  public:
    ASP_Engine(){};
   ~ASP_Engine(){};

  void run_on_file(string data_filename, string output_filename, string pattern_type){
    string program;
    if (pattern_type == "closed"){
      program = "asp_encodings/closed_post_processing.asp";
    }
    string command = "clingo " + program + " " + data_filename + " > " + output_filename;     
    cout << "executing... " + command + "\n";
    system(command.c_str());
  }
};
