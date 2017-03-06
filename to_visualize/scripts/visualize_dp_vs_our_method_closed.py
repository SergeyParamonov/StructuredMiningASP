import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def main():
    datasets = []
    dp_mushroom_closed  = pd.read_csv("dominance_programming/mushroom.txt_dp_runtime_closed")
    dp_vote_closed      = pd.read_csv("dominance_programming/vote.txt_dp_runtime_closed")
    our_method          = pd.read_csv("itemset_our_method/mushroom.txt_itemset_runtimes.txt")
    our_methodvote      = pd.read_csv("itemset_our_method/vote.txt_itemset_runtimes.txt")
    sns.set(font_scale=3.5)
    sns.set_style("whitegrid")
    closed = our_method[our_method['pattern_type'] == "closed"]
    closedvote = our_methodvote[our_methodvote['pattern_type'] == "closed"]
    plt.plot(closed['threshold']/100,closed['time'], linestyle='-', marker="o", markersize=30, color="red",markeredgecolor='black',markeredgewidth=1.0)
    plt.plot(closedvote['threshold']/100,closedvote['time'], linestyle='-', marker="s", markersize=30, color="red",markeredgecolor='black',markeredgewidth=1.0)
    plt.plot(dp_mushroom_closed['support'],dp_mushroom_closed['time'], linestyle='-', marker=">", markersize=30, color="blue",markeredgecolor='black',markeredgewidth=1.0)
    plt.plot(dp_vote_closed['support'],dp_vote_closed['time'], linestyle='-', marker="<", markersize=30, color="blue",markeredgecolor='black',markeredgewidth=1.0)
    

    plt.xlim(plt.xlim()[0]-0.005, plt.xlim()[1]+0.005)
#   plt.ylim(0.8, plt.ylim()[1])
    plt.legend(labels=["Our Method: Mushrooms", "Our Method: Vote","DP: Mushrooms","DP: Vote"],loc='best')
    plt.xlabel("Frequency")
    plt.ylabel("Runtime in Seconds")
    plt.yscale('log')
    plt.show()

if __name__ == "__main__":
    main()
