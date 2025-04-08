import pandas as pd
import numpy as np
import random


data = pd.read_csv("../Raw Data Sets/HealthcareDatasetStrokeData.csv")


def printf(x):
    pd.set_option('display.max_rows', len(x))
    pd.set_option('display.max_columns', len(x))
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns', len(x))


def randomSampling(df, n_samples):
    n = min(n_samples, len(df))
    sample_set1 = df.sample(n_samples)
    #these won't do repetition of datapoints
    sample_set2 = df.sample(n_samples, replace=True, random_state=45)
    #this won't replace, i.e. repetition may occur
    #random_state = seed

    return sample_set1, sample_set2


def stratSampling(df, n_samples, col):
    n = min(n_samples, df[col].value_counts().min())
    #Deals with the exceptions when the n_samples provided > no. of elements in the smallest strata.
    df_groupby = df.groupby(col).apply(lambda x: x.sample(n=n), include_groups=False)
    return df_groupby


def clusterSampling(df, cluster_list, col):
    sample_set = df[df[col].isin(cluster_list)]
    return sample_set


def systematicSampling(df, n_samples):
    total = len(df)
    interval = total // n_samples

    indexes = np.arange(0, total, step=interval)
    systematic_sample = df.iloc[indexes]

    return systematic_sample


printf(data)
