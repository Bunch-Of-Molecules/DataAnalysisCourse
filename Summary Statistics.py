import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

wholesale_data = pd.read_csv("Raw Data Sets/Wholesale_customers.csv")

column_heads = list(wholesale_data)

#----------------------------------------------------------------------#
#making dictionaries containing the sales in each category
max_dict = {}
sum_dict = {}


def max_dic(data, dic):
    for i in range(2, 8, 1):
        dic[column_heads[i]] = max(data[column_heads[i]])


def sum_dic(data, dic):
    for i in range(2, 8, 1):
        dic[column_heads[i]] = sum(data[column_heads[i]])


max_dic(wholesale_data, max_dict)

sum_dic(wholesale_data, sum_dict)
maxSaleCategory = max(sum_dict, key=sum_dict.get)


#plots two given datasets in one window. positioning not configurable.
def two_row_plotter(x1, y1, x2, y2, title1="Graph 1", title2="Graph 2"):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))  # read documentation for more use case examples

    ax1.bar(x1, y1, align="center", width=0.5)
    ax1.set_title(title1)
    ax2.bar(x2, y2, align="center", width=0.5)
    ax2.set_title(title2)

    plt.show()


#two_row_plotter(x1=list(max_dict.keys()), y1=list(max_dict.values()), x2=list(sum_dict.keys()), y2=list(sum_dict.values()))


#plots mean, median, max, min and iqr as lines with data points
def summary_stats_1(data, col):
    year_avg = np.mean(data[col])
    year_med = np.median(data[col])
    year_max = max(data[col])
    year_min = min(data[col])
    year_iqr = np.percentile(data[col], [75])[0] - np.percentile(data[col], [25])[0]

    fix, ax = plt.subplots(figsize=(15, 6))
    plt.scatter(data.index, data[col], marker="^")

    ax.axhline(y=year_avg, label="Mean", color="deeppink", linestyle="--", linewidth=2)
    ax.axhline(y=year_med, label="Median", color="black", linewidth=2)
    ax.axhline(y=year_max, label="Max", color="blue", linewidth=2, linestyle="-")
    ax.axhline(y=year_min, label="Min", color="tomato", linewidth=2, linestyle=":")
    ax.axhline(y=year_iqr, label="Inter-quartile Range", color="cyan", linewidth=2, linestyle="-.")

    ax.legend()
    plt.show()


#plots mean, std, and sigma+-1 lines with the given distribution
def summary_stats_2(data, col):
    stddev = scipy.stats.tstd(data[col])
    mean = np.mean(data[col])
    stddev_plus_one = mean + stddev
    stddev_minus_one = mean - stddev
    standard_error_mean = scipy.stats.sem(data[col])
    #sem is an estimate of far a mean of a particular sample of a population differs from the mean of the population
    #in case where data about the population is not given,
    #sem = std/sqrt(no. of data points in samples)

    fix, ax = plt.subplots(figsize=(8, 6))
    plt.scatter(data.index, data[col], marker=".")

    ax.axhline(y=mean, label="Mean", color="deeppink", linestyle="-", linewidth=2)
    ax.axhline(y=stddev_plus_one, label="μ + σ", color="black", linewidth=2)
    ax.axhline(y=stddev_minus_one, label="μ - σ", color="blue", linewidth=2, linestyle="-")
    ax.axhline(y=standard_error_mean, label="Standard Error \n of Mean", color="red", linewidth=2, linestyle="-.")

    ax.legend()
    plt.show()


#returns the percentage of data points within (μ - σ ,μ + σ) from entire data
def normal_or_no(data, col):
    stddev = scipy.stats.tstd(data[col])
    mean = np.mean(data[col])
    stddev_plus_one = mean + stddev
    stddev_minus_one = mean - stddev

    ar_len = len(data[col])

    c = 0

    for i in range(0, ar_len - 1, 1):
        if stddev_plus_one > data[col][i] > stddev_minus_one:
            c += 1

    percentage = (c / ar_len) * 100
    return percentage

