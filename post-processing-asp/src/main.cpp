#include "miners.cpp"


int main(){
  Miner *miner = new ItemsetMiner();
  miner->run_solver();
  return 0;
}
