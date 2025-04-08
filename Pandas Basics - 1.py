import pandas as pd

def printer(variables):
    for var in variables:
        print(var)
        print("")


#Pandas has 3 data structures: Series, Data Frame and Panel

#--------Series--------: A Single dimensional data structure#


x = [2, 3, 4, 5, 6, 7]
dic = {"Name": ["Harry", "Polly", "Molly", "Dolly", "Jolly"],
       "Age": [13, 14, 13, 14, 14],
       "School": ["GHS", "GHS", "GHS", "JHS", "JHS"],
       "Rank": [2, 1, 3, 1, 2]}

var_1 = pd.Series(x, index=["q", 5, "r", True, 6, 7], dtype="float", name="Tis my name")
#converting a list to a pandas series

var_2 = pd.Series(dic)
#converting a dictionary to a series

var_3 = pd.Series(6, index=[1, 2, 3, 4, 5, 6, "q"], name="Just Numbers")
#converting a single data to a series

var_4 = var_1 + var_3
#we see that this operation, despite having missing values, doesn't throw an error and accounts for the missing data


#------Data-Frames-----------: A Two dimensional data structure#


var_5 = pd.DataFrame(x)
#Using a simple list as data

var_6 = pd.DataFrame(dic, columns=["Name", "School", "Rank"], index=[1, 2, 3, 4, 5])
#Using a simple dictionary as data, but printing only selected columns

var_7 = pd.DataFrame([var_1, var_3])
#Using 2 Series to construct a data frame
#And as it turns out, it MATCHES the indexes as well, same indexed values are together...

print(var_7[2]["Tis my name"])
#getter method

# just do operations by using <structure name>[Column Index] = <structure name>[Column Index] +-/* <structure name>
# [Column Index]

var_8 = pd.DataFrame({"A": [1, 2, 3, 4, 5],
                      "B": [5, 6, 7, 8, 9]})
var_8.insert(1, 'Inserted', var_8["B"])
#Column Insertion
#But like previous examples where it didn't throw an error when data was missing, now it will - so match the data length

var_8["D"] = var_8["A"][1:4]
#slicing performed on lists as:
#list_name[starting_index : ending_index+1]
#performing selective data retrieval via slicing

var_8.loc[0, "D"] = 100
var_8.loc[4, "D"] = 100

#use pop and del for deletion

del var_8["Inserted"]
var_8.pop("B")

list_of_values = [var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8]
printer(list_of_values)
