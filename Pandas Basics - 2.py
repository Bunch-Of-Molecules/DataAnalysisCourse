import pandas as pd
import random

dic = {1: ["Person1", "Person2", "Person3", "Person4", "Person5"],
       2: [23, 45, 23, 65, 24],
       3: [1340000.00, 2500000.00, 1050924.00, 300000.00, 958753.00],
       4: ["City1", "City1", "City2", "City1", "City2"]}


#--------Writing CSV Files-------#

def Write_to_csv(data, name):
    df = pd.DataFrame(data)
    df.to_csv(path_or_buf=name + ".csv", index=False)


#--------Reading CSV Files---------#

def Reading_a_csv(path):
    data_1 = pd.read_csv(path)

    print(data_1.columns)
    print()
    print(data_1.describe())
    print()

    print(data_1.head(n=7))
    print()
    #Gets the first n rows
    print(data_1.tail(n=3))
    print()
    #Gets the last n rows
    print(data_1[0:4])
    print()
    #can use slicing as well

    data_1.loc[3, "PRODUCT"] = "brocolli"
    #Setter and Getter method
    var = data_1.loc[:, " QUANTITY (pound)"]
    print(data_1)
    print(var)


#use drop() to remove stuff
#------Dealing with missing data----#


def Missing_data_handling(path):
    data = pd.read_csv(path)
    data.dropna(inplace=True, how="all")
    #drops all Nan values

    print(data)


#-----Group By Function------#
def Grouping_Random_data(path):
    data = pd.read_csv(path)
    grouped_data = data.groupby("City")

    return grouped_data


Reading_a_csv("Raw Data Sets/prices.csv")