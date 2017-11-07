import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def main():
    datasets   = []
    wasp_mushrooms  = pd.read_csv("WASP_results/mushrooms_wasp.csv")
    wasp_vote       = pd.read_csv("WASP_results/vote_wasp.csv")
    clasp_mushrooms = pd.read_csv("itemset_our_method/mushroom.txt_itemset_runtimes.txt")
    clasp_vote = pd.read_csv("itemset_our_method/vote.txt_itemset_runtimes.txt")
    sns.set(font_scale=3.5)
    sns.set_style("whitegrid")

    clasp_mushrooms = clasp_mushrooms[clasp_mushrooms['pattern_type'] == "maximal"]
    clasp_vote      = clasp_vote[clasp_vote['pattern_type'] == "maximal"]

    wasp_mushrooms = wasp_mushrooms[wasp_mushrooms['pattern_type'] == "maximal"]
    wasp_vote      = wasp_vote[wasp_vote['pattern_type'] == "maximal"]

    plt.plot(clasp_mushrooms['threshold']/100,clasp_mushrooms['time'], linestyle='-', marker="o", markersize=30, color="red",markeredgecolor='black',markeredgewidth=1.0)
    plt.plot(clasp_vote['threshold']/100,clasp_vote['time'], linestyle='-', marker="s", markersize=30, color="red",markeredgecolor='black',markeredgewidth=1.0)
    plt.plot(wasp_mushrooms['threshold']/100,wasp_mushrooms['time'], linestyle='-', marker=">", markersize=30, color="blue",markeredgecolor='black',markeredgewidth=1.0)
    plt.plot(wasp_vote['threshold']/100,wasp_vote['time'], linestyle='-', marker="<", markersize=30, color="blue",markeredgecolor='black',markeredgewidth=1.0)
    

    plt.xlim(plt.xlim()[0]-0.005, plt.xlim()[1]+0.005)
#   plt.ylim(0.8, plt.ylim()[1])
    plt.legend(labels=["Clasp: Mushrooms", "Clasp: Vote","WASP: Mushrooms","WASP: Vote"],loc='best')
    plt.xlabel("Frequency")
    plt.ylabel("Runtime in Seconds")
    plt.yscale('log')
    plt.show()

if __name__ == "__main__":
    main()
