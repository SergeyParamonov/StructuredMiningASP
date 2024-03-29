#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
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
    virtual int get_id(){}
};

class Sequence: public Pattern{

  private:
    vector<int> items;
    int frequency;
    string original_line;
    int id;
    int size;
  public:
    static int global_id;

   Sequence(const Sequence &other){
       original_line = other.original_line;
       frequency = other.frequency;
       items     = other.items;
       size      = other.size;
     }

    Sequence(string line_to_parse){
       id = global_id;
       global_id++;
       vector<string> strs;
       original_line = line_to_parse;
       line_to_parse.erase(remove(line_to_parse.begin(), line_to_parse.end(), '<'), line_to_parse.end());
       line_to_parse.erase(remove(line_to_parse.begin(), line_to_parse.end(), '>'), line_to_parse.end());


       boost::split(strs, line_to_parse, boost::is_any_of(" :"));
       frequency = atoi(strs.back().c_str());
       strs.pop_back();
       size = 0;

       for (string s:strs){
          if (s != ""){
            int val = atoi(s.c_str());
            items.push_back(val);
            size += 1;
          }
       }
     }
    Sequence & operator=(const Sequence& that){
        if (this == &that){
          return *this;
        }
        original_line = that.original_line;
        frequency = that.frequency;
        items = that.items;
        size = that.size;
        return *this;
     }

     ~Sequence(){
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

     string make_ASP_str(){
       string asp_repr = (boost::format("pattern(%1%).") % id).str(); 
       asp_repr += (boost::format(" support(%1%,%2%).") % id % frequency).str(); 
       for (int i=0; i < items.size(); i++){
          asp_repr += (boost::format(" item(%1%,%2%,%3%).") % id % i % items[i]).str();
       }
       asp_repr += (boost::format(" size(%1%,%2%).") % id % size).str();
       asp_repr += "\n";
       return asp_repr;
     }
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
      id = other.id;
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
int Sequence::global_id = 1;
