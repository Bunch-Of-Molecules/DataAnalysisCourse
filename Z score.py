import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import pandas as pd

bill_data = pd.read_csv("../Raw Data Sets/prices.csv")

bill_data["Per Pound Price"] = bill_data["RETAIL PRICE(dollars)"]/bill_data["QUANTITY (pound)"]
bill_data["Z Score"] = scipy.stats.zscore(bill_data["Per Pound Price"])

print(bill_data)

"""
Z Score is a good measure to tell where a value stands with respect to others in a dataset.
Z Score is actually how many standard deviations a value is from the mean.
"""
