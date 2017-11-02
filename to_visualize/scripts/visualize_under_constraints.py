import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def main():
    general_mushrooms = pd.read_csv("itemset_our_method/mushroom.txt_itemset_runtimes.txt")
    closed_mushrooms  = general_mushrooms[general_mushrooms['pattern_type'] == "closed"]

    general_vote = pd.read_csv("itemset_our_method/vote.txt_itemset_runtimes.txt")
    closed_vote  = general_vote[general_vote['pattern_type'] == "closed"]

    mushrooms_under_constrains =  pd.read_csv("under_constraints/mushroom.txt_itemset_runtimes.txt")
    vote_under_constrains      =  pd.read_csv("under_constraints/vote.txt_itemset_runtimes.txt")

    

    sns.set(font_scale=3.5)
    sns.set_style("whitegrid")
    plt.plot(closed_mushrooms['threshold']/100,closed_mushrooms['time'], linestyle='-', marker='s', markersize=30, color='red')
    plt.plot(mushrooms_under_constrains['threshold']/100,mushrooms_under_constrains['time'], linestyle='-', marker='o', markersize=30, color='blue')

    plt.plot(closed_vote['threshold']/100,closed_vote['time'], linestyle='-', marker='d', markersize=30, color='red')
    plt.plot(vote_under_constrains['threshold']/100,vote_under_constrains['time'], linestyle='-', marker='*', markersize=37, color='blue')

    plt.xlim(plt.xlim()[0]-0.01, plt.xlim()[1]+0.01)
    plt.ylim(0.80, plt.ylim()[1]+200)
    plt.legend(labels=["Mushrooms w/o local constraints", "Mushrooms under constraints", "Vote w/o local constraints", "Vote under constraints"],loc='best')
    plt.xlabel("Frequency")
    plt.ylabel("Runtime in Seconds")
    plt.yscale('log')
    plt.show()

if __name__ == "__main__":
    main()
