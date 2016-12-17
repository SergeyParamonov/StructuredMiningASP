import sys
from os import listdir

def process_input_dataset(inputdataset):
    with open(inputdataset, "r") as dataset:
        data = dataset.read().splitlines()
        for line in data:
            if "@" in line:
                continue
            if not line:
                continue
            items = line.split()
            items = items[:-1]
            yield items

def cut_txt(string):
    return string.replace(".txt","")


def write_dataset_in_asp_and_txt_format(input_dataset, output_dataset):
    with open(output_dataset+".asp", "w") as asp_dataset, open(output_dataset+".txt","w") as txt_output:
        for index,itemset in enumerate(process_input_dataset(input_dataset)):
           print(" ".join(itemset),file=txt_output)
           print(" ".join(["db({t},{i}).".format(t=index,i=item) for item in itemset]),file=asp_dataset)

def get_input_output_pairs(input_folder, output_folder):
    files = listdir(input_folder)
    for afile in files:
        full_input_path = input_folder + "/" + afile
        full_output_path = output_folder + "/" + cut_txt(afile)
        yield (full_input_path,full_output_path)
    


def main():
    raw_dataset_folder = "datasets/raw_downloaded_itemsets"
    dataset_folder = "datasets/itemsets"

    for input_dataset,output_dataset in get_input_output_pairs(raw_dataset_folder, dataset_folder):
        write_dataset_in_asp_and_txt_format(input_dataset,output_dataset)


if __name__ == "__main__":
    main()
