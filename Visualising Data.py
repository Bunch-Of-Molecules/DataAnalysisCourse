import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

month_list = {"01": "Jan",
              "02": "Feb",
              "03": "Mar",
              "04": "Apr",
              "05": "May",
              "06": "Jun",
              "07": "Jul",
              "08": "Aug",
              "09": "Sep",
              "10": "Oct",
              "11": "Nov",
              "12": "Dec"}


def Write_to_csv(dataframe, name):
    df = pd.DataFrame(dataframe)
    df.to_csv(path_or_buf=name + ".csv", index=False)


def sorter(dataset, column):
    for i in range(0, 254, 1):
        for j in range(0, 253, 1):
            if dataset[column][j] > dataset[column][j + 1]:
                temp = dataset[column][j]
                dataset.loc[j, column] = dataset.loc[j + 1, column]
                dataset.loc[j + 1, column] = temp


def month_maker(dataset, col):
    for i in range(0, 254, 1):
        dataset.loc[i, col] = month_list[dataset[col][i][5:7]]
