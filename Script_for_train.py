import pandas as pd
import os
import matplotlib.pyplot as plt

way_to_data = input("Print way to your data: ")

data_to_analysis = pd.read_csv(way_to_data)

print(data_to_analysis.head())


def base_distribution(data_set):

    dict_of_nucl = data_set[["A","T","G","C"]]


    dict_of_nucl.index = data_set["pos"].values
    dict_of_nucl.plot.bar(stacked=True, figsize=(10, 6))

    plt.show()

def part_of_data(way, data_set):

    path, file_type = os.path.splitext(way)

    mean_pos = data_set["pos"].mean()
    part = data_set.loc[(data_set["matches"] > mean_pos)][["matches", "reads_all",
                                                           "mismatches", "deletions", "insertions"]]
    part.to_csv(path+ "_part"+ file_type)




base_distribution(data_to_analysis)
part_of_data(way_to_data,data_to_analysis)
