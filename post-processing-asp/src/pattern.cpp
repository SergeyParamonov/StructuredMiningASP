#include <stdlib.h>
#include <iostream>
#include <vector>
#include <boost/algorithm/string.hpp>
#include <boost/format.hpp>

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
    virtual string make_ASP_str(){}
    virtual string make_selected_ASP_repr(){}
    virtual int get_id(){}
};

class Itemset : public Pattern{
  private:
    vector<int> items;
    int frequency;
    string original_line;
    int id;
    int size;
  public:
    static int global_id;
     
     Itemset(const Itemset &other){
       original_line = other.original_line;
       frequency = other.frequency;
       items =  other.items;
       size = other.size;
     }
     
     Itemset(string line_to_parse){
       id = global_id;
       global_id++;
       vector<string> strs;
       original_line = line_to_parse;
       boost::split(strs, line_to_parse, boost::is_any_of(" :"));
       frequency = atoi(strs.back().c_str());
       strs.pop_back();
       size = 0;
       for (string s:strs){
          int val = atoi(s.c_str());
          items.push_back(val);
          size += 1;
       }
     }

     Itemset & operator=(const Itemset& that){
        if (this == &that){
          return *this;
        }
        original_line = that.original_line;
        frequency = that.frequency;
        items = that.items;
        size = that.size;
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

     int get_id(){
       return id;
     }

     vector<int> get_items(){
       return items;
     }

     string make_selected_ASP_repr(){
       string asp_repr = (boost::format("selected_pattern(%1%).") % id).str(); 
       asp_repr += (boost::format(" selected_support(%1%).") % frequency).str(); 
       for (auto i: items){
          asp_repr += (boost::format(" selected_item(%1%).") % i).str();
       }
       asp_repr += (boost::format(" selected_size(%1%).") % size).str();
       asp_repr += "\n";
       return asp_repr;
     }

     string make_ASP_str(){
       string asp_repr = (boost::format("pattern(%1%).") % id).str(); 
       asp_repr += (boost::format(" support(%1%,%2%).") % id % frequency).str(); 
       for (auto i: items){
          asp_repr += (boost::format(" item(%1%,%2%).") % id % i).str();
       }
       asp_repr += (boost::format(" size(%1%,%2%).") % id % size).str();
       asp_repr += "\n";
       return asp_repr;
     }
};

int Itemset::global_id = 1;
