import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def main():
    datasets   = []
    wasp_jmlr  = pd.read_csv("wasp_sequences/jmlr.csv")
    wasp_iprg  = pd.read_csv("wasp_sequences/iprg.csv")
    clasp_jmlr = pd.read_csv("our_sequences/jmlr_almost_all.txt")
    clasp_iprg = pd.read_csv("our_sequences/iprg.dat_sequence_runtimes.txt")
    sns.set(font_scale=3.5)
    sns.set_style("whitegrid")

    clasp_jmlr = clasp_jmlr[clasp_jmlr['pattern_type'] == "maximal"]
    clasp_iprg      = clasp_iprg[clasp_iprg['pattern_type'] == "maximal"]

    wasp_jmlr = wasp_jmlr[wasp_jmlr['pattern_type'] == "maximal"]
    wasp_iprg      = wasp_iprg[wasp_iprg['pattern_type'] == "maximal"]

    plt.plot(clasp_jmlr['threshold']/100,clasp_jmlr['time'], linestyle='-', marker="o", markersize=30, color="red",markeredgecolor='black',markeredgewidth=1.0)
    plt.plot(clasp_iprg['threshold']/100,clasp_iprg['time'], linestyle='-', marker="s", markersize=30, color="red",markeredgecolor='black',markeredgewidth=1.0)
    plt.plot(wasp_jmlr['threshold']/100,wasp_jmlr['time'], linestyle='-', marker=">", markersize=30, color="blue",markeredgecolor='black',markeredgewidth=1.0)
    plt.plot(wasp_iprg['threshold']/100,wasp_iprg['time'], linestyle='-', marker="<", markersize=30, color="blue",markeredgecolor='black',markeredgewidth=1.0)
    

#   plt.xlim(0.040,0.160)
    plt.ylim(0.5, plt.ylim()[1]*1.20)
    plt.legend(labels=["Clasp: jmlr", "Clasp: iprg","WASP: jmlr","WASP: iprg"],loc='best')
    plt.xlabel("Frequency")
    plt.ylabel("Runtime in Seconds")
    plt.yscale('log')
    plt.show()

if __name__ == "__main__":
    main()
