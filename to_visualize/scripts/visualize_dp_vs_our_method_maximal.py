import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def main():
    datasets = []
    dp_mushroom_maximal  = pd.read_csv("dominance_programming/mushroom.txt_dp_runtime_maximal")
    dp_vote_maximal      = pd.read_csv("dominance_programming/vote.txt_dp_runtime_maximal")
    our_method          = pd.read_csv("itemset_our_method/mushroom.txt_itemset_runtimes.txt")
    our_methodvote      = pd.read_csv("itemset_our_method/vote.txt_itemset_runtimes.txt")
    sns.set(font_scale=3.5)
    sns.set_style("whitegrid")
    maximal = our_method[our_method['pattern_type'] == "maximal"]
    maximalvote = our_methodvote[our_methodvote['pattern_type'] == "maximal"]
    plt.plot(maximal['threshold']/100,maximal['time'], linestyle='-', marker="o", markersize=30, color="red",markeredgecolor='black',markeredgewidth=1.0)
    plt.plot(maximalvote['threshold']/100,maximalvote['time'], linestyle='-', marker="s", markersize=30, color="red",markeredgecolor='black',markeredgewidth=1.0)
    plt.plot(dp_mushroom_maximal['support'],dp_mushroom_maximal['time'], linestyle='-', marker=">", markersize=30, color="blue",markeredgecolor='black',markeredgewidth=1.0)
    plt.plot(dp_vote_maximal['support'],dp_vote_maximal['time'], linestyle='-', marker="<", markersize=30, color="blue",markeredgecolor='black',markeredgewidth=1.0)
    

    plt.xlim(plt.xlim()[0]-0.005, plt.xlim()[1]+0.005)
#   plt.ylim(0.8, plt.ylim()[1])
    plt.legend(labels=["Our Method: Mushrooms", "Our Method: Vote","DP: Mushrooms","DP: Vote"],loc='best')
    plt.xlabel("Frequency")
    plt.ylabel("Runtime in Seconds")
    plt.yscale('log')
    plt.show()

if __name__ == "__main__":
    main()
