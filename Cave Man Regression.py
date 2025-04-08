from random import shuffle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

ecom_data = pd.read_csv("../Raw Data Sets/Ecommerce Customers.csv")

corr_mat = ecom_data.corr(numeric_only=True)
#elements along principal diagonal are one.

"""sns.heatmap(corr_mat, annot=True, ax=ax)"""
#to clearly visualise which two columns in our dataset show the highest correlation

# sns.scatterplot(data=ecom_data, x='Length of Membership', y='Yearly Amount Spent')
# plt.xlabel('Length of membership')
# plt.ylabel('Yearly Amount Spent')

#now that we know we want to play with only these two columns,
#the other columns can go fuck themselves
#also lets shuffle the data a bit, so that there's no relationship coded in the order of the data

ecom_data = ecom_data[['Length of Membership', 'Yearly Amount Spent']]
shuffled_df = ecom_data.sample(frac=1, random_state=67)

#making the training the dataset
#training the dataset helps avoid overfitting

train_size = int(len(shuffled_df) * 0.7)
train_set = shuffled_df[:train_size]

test_set = shuffled_df[train_size:]

"""vvv helper functions vvv """
def mean(values):
    return sum(values) / float(len(values))

def covariance(x, mean_x, y, mean_y):
    numerator = 0.0

    for i in range(len(x)):
        numerator += (x[i] - mean_x) * (y[i] - mean_y)

    return numerator / len(x)

def variance(values, _mean):
    return sum([(x - _mean) ** 2 for x in values]) / len(values)

"""/"""

def coefficients(dataset):
    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset]

    x_mean, y_mean = mean(x), mean(y)

    _slope = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
    _intercept = y_mean - _slope * x_mean

    return [_intercept, _slope]

train_set = train_set.to_numpy()
test_set = test_set.to_numpy()

intercept, slope = coefficients(train_set)

x = train_set[:, 0]
y = train_set[:, 1]

# plt.plot(x, y, 'ro')
# plt.plot(x, slope*x + intercept)


def make_prediction(train, test):
    predictions = []

    intercept_, slope_ = coefficients(train)

    for row in test:
        y_pred = intercept_ + slope_ * row[0]
        predictions.append(y_pred)

    return predictions

y_predicted = make_prediction(train_set, test_set)
y_predicted = np.array(y_predicted)

y_test = test_set[:, 1]


data_actual_prediction = pd.DataFrame({'Actual Values' : y_test,'Predicted Values' : y_predicted})

ax = plt.subplots(figsize=(10, 8))

# sns.lineplot(x = data_actual_prediction.index, y = 'Predicted Values', color='green', data = data_actual_prediction)
# sns.lineplot(x = data_actual_prediction.index, y = 'Actual Values', color='blue', data = data_actual_prediction)

# plt.legend(['Actual Values', 'Predicted Values'])

def calc_mse(y_pred, y_actual):
    error = np.square(np.subtract(y_actual, y_pred)).mean()
    return error

#mse is essentially the variance of the residuals
#rmse is the deviation of the residuals

def calc_r_square(y_pred, y_actual):
    sst = np.sum((y_actual - y_actual.mean()) ** 2) #total sum of squares
    ssr = np.sum((y_pred - y_actual) ** 2) #residual sum of squares

    r_sq = 1 - ssr/sst
    return r_sq #coefficient of determination

print(calc_r_square(y_predicted, y_test))
#whatever percentage this function this give can be interpreted as:
# "__% of the variance of y is explained by x variable"

# sns.histplot(data = (y_test-y_predicted), kde=True, legend=False, color="red")
sns.residplot(x = y_predicted, y = y_test-y_predicted)
# the scatter plot of the residuals should be as random as possible, there shouldn't be any pattern present
# this is a sign of a good regression analysis

#kde = kernel density estimation
plt.show()