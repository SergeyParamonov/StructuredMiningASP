import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def main():
    asp_torsten = pd.read_csv("asp_torsten/asp_200_closed.csv")
    our_method  = pd.read_csv("our_sequences/asp_200.dat_sequence_runtimes.txt")
    closed = our_method[our_method['pattern_type'] == "closed"]
    sns.set(font_scale=3)
    sns.set_style("whitegrid")
    plt.plot(asp_torsten['frequency'],asp_torsten['time'],linestyle='-', marker='o', markersize=25, color='blue')
    plt.plot(closed['threshold']/100,closed['time'], linestyle='-', marker='d', markersize=25, color='red')
    plt.xlim(plt.xlim()[0]-0.01, plt.xlim()[1]+0.01)
    plt.ylim(0, plt.ylim()[1]+10)
    plt.legend(labels=["ASP Model (Gebser et al. 2016)", "Our ASP Model"],loc='best')
    plt.xlabel("Frequency")
    plt.ylabel("Runtime in Seconds")
    plt.show()

if __name__ == "__main__":
    main()
