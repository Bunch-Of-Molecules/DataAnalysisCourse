from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ecom_data = pd.read_csv("../Raw Data Sets/Ecommerce Customers.csv")

ecom_data = ecom_data[['Length of Membership', 'Yearly Amount Spent']]
shuffled_df = ecom_data.sample(frac=1, random_state=67)

train_size = int(len(shuffled_df) * 0.7)

train_set = shuffled_df[:train_size].to_numpy()
test_set = shuffled_df[train_size:].to_numpy()

X_train = train_set[:, 0]
X_train = X_train.reshape((-1,1)) # -1 is telling the code to use its own brain use whatever shape it needs

Y_train = train_set[:, 1]
Y_train = Y_train.reshape((-1,1))
""" 
We needed to reshape these cuz sklearn needs 1D arrays as input, so we turn the 2D array 
train set into individual 1D arrays of x and y.
"""
X_test = test_set[:, 0]
X_test = X_test.reshape((-1,1))

Y_test = test_set[:, 1]
Y_test = Y_test.reshape((-1,1))

lr = LinearRegression()
linear_reg_model = lr.fit(X_train, Y_train)

# print(linear_reg_model.coef_)
# print(linear_reg_model.intercept_)

y_pred = lr.predict(X_test)

# print(f"Training score: {linear_reg_model.score(X_train, Y_train)}")
# print(f"Mean Sqaured Error: {mean_squared_error(Y_train, linear_reg_model.predict(X_train))}")
# print(f"RMSE: {math.sqrt(mean_squared_error(Y_train, linear_reg_model.predict(X_train)))}")