import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def main():
    datasets = []
    dp_skyline = pd.read_csv("dominance_programming/vote.txt_dp_runtime_skyline")
    dp_skyline_plus = pd.read_csv("dominance_programming/vote.txt_dp_runtime_skyline+")
    our_method      = pd.read_csv("itemset_our_method/vote.txt_itemset_runtimes.txt")
    sns.set(font_scale=3.5)
    sns.set_style("whitegrid")
    skyline = our_method[our_method['pattern_type'] == "skyline"]
    plt.plot(skyline['threshold']/100,skyline['time'], linestyle='-', marker="o", markersize=30, color="red",markeredgecolor='black',markeredgewidth=1.0)
    plt.plot(dp_skyline['support'],dp_skyline['time'], linestyle='-', marker="s", markersize=30, color="blue",markeredgecolor='black',markeredgewidth=1.0)
    plt.plot(dp_skyline_plus['support'],dp_skyline_plus['time'], linestyle='-', marker="d", markersize=30, color="blue",markeredgecolor='black',markeredgewidth=1.0)
    

    plt.xlim(plt.xlim()[0]-0.005, plt.xlim()[1]+0.005)
#   plt.ylim(0.8, plt.ylim()[1])
    plt.legend(labels=["Our Method: Vote","DP out-of-the-box: Vote ","DP fine-tuned: Vote"],loc='best')
    plt.xlabel("Frequency")
    plt.ylabel("Runtime in Seconds")
    plt.yscale('log')
    plt.show()

if __name__ == "__main__":
    main()
