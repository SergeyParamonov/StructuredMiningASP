import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def main():
    datasets = []
    dp_mushroom_closed  = pd.read_csv("dominance_programming/mushroom.txt_dp_runtime_closed")
    dp_mushroom_maximal = pd.read_csv("dominance_programming/mushroom.txt_dp_runtime_maximal")
    our_method          = pd.read_csv("itemset_our_method/mushroom.txt_itemset_runtimes.txt")
    sns.set(font_scale=3)
    sns.set_style("whitegrid")
    closed = our_method[our_method['pattern_type'] == "closed"]
    plt.plot(closed['threshold']/100,closed['time'], linestyle='-', marker="s", markersize=25, color="red")
    plt.plot(dp_mushroom_closed['threshold']/100,dp_mushroom_closed['time'], linestyle='-', marker="s", markersize=25, color="red")
    

#   plt.xlim(plt.xlim()[0]-0.005, plt.xlim()[1]+0.005)
#   plt.ylim(0.8, plt.ylim()[1])
#   plt.legend(labels=["Our Method", "IPRG","Unix Users"],loc='best')
    plt.xlabel("Frequency")
    plt.ylabel("Runtime in Seconds")
    plt.yscale('log')
    plt.show()

if __name__ == "__main__":
    main()
