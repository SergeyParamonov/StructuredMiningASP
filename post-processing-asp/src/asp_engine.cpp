#include <stdlib.h>

class ASP_Engine{
  public:
    ASP_Engine(){};
   ~ASP_Engine(){};

  void run_on_file(string filename, string output_filename){
    string command = "clingo " + filename + " > " + output_filename;     
    cout << "executing... " + command + "\n";
    system(command.c_str());
  }
};
