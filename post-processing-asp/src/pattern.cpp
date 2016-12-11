#include <stdlib.h>
#include <iostream>
#include <vector>
#include <boost/algorithm/string.hpp>

using namespace std;
class Pattern{
  public:  
    Pattern(){}
    Pattern(string line_to_parse){}
    Pattern(const Pattern &other){}
    Pattern & operator=(const Pattern& that){}
    ~Pattern(){}
   virtual string to_string(){}
   virtual int get_frequency(){}
   virtual vector<int> get_items(){}
};

class Itemset : public Pattern{
  private:
    vector<int> items;
    int frequency;
    string original_line;
  public:
     
     Itemset(const Itemset &other){
       original_line = other.original_line;
       frequency = other.frequency;
       items =  other.items;
     }
     
     Itemset(string line_to_parse){
       vector<string> strs;
       original_line = line_to_parse;
       boost::split(strs, line_to_parse, boost::is_any_of(" :"));
       frequency = atoi(strs.back().c_str());
       strs.pop_back();
       for (string s:strs){
          int val = atoi(s.c_str());
          items.push_back(val);
       }
     }

     Itemset & operator=(const Itemset& that){
        if (this == &that){
          return *this;
        }
        original_line = that.original_line;
        frequency = that.frequency;
        items = that.items;
        return *this;
     }

     ~Itemset(){
       items.clear();
     }
     string to_string(){
       return original_line;
     }
     int get_frequency(){
       return frequency;
     }
     vector<int> get_items(){
       return items;
     }
};
