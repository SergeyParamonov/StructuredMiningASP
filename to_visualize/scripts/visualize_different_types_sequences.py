import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def main():
    datasets = []
    datasets.append(pd.read_csv("our_sequences/jmlr_almost_all.txt"))
    datasets.append(pd.read_csv("our_sequences/iprg.dat_sequence_runtimes.txt"))
    datasets.append(pd.read_csv("our_sequences/unix_users.dat_sequence_runtimes.txt"))
    sns.set(font_scale=3)
    sns.set_style("whitegrid")
    colors = ["red","blue",'green']
    markers = ['o','s','d']
    for pattern_type in ['closed','maximal','skyline']:
      for i,dataset in enumerate(datasets):
        subset = dataset[dataset['pattern_type'] == pattern_type]
        plt.plot(subset['threshold']/100,subset['time'], linestyle='-', marker=markers[i], markersize=25, color=colors[i])

      plt.xlim(0.047, 0.155)
      plt.ylim(0.8, plt.ylim()[1]+20)
      plt.legend(labels=["JMLR", "IPRG","Unix Users"],loc='best')
      plt.xlabel("Frequency")
      plt.xticks(list(np.arange(0.05,0.16,0.01)))
      plt.ylabel("Runtime in Seconds")
      plt.yscale('log')
      plt.show()

if __name__ == "__main__":
    main()
