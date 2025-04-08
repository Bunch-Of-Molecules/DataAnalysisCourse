import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

wholesale_data = pd.read_csv("../Raw Data Sets/Wholesale_customers.csv")

"""
Correlation and covariance are measures of linear+ relationship between the given datasets
Correlation is just a normalised version of covariance.
-1<cor<1   and  -infi<cov<+infi
"""

print(np.corrcoef(wholesale_data["Frozen"], wholesale_data["Grocery"]))
print()
print(np.cov(wholesale_data["Fresh"], wholesale_data["Frozen"]))
print()

"""
The output is of form of a matrix/a two-dimensional array
When comparing two, we see the output as:
|1, var|
|var, 1|
"1" here is just the first argument compared with itself, var is ar1 and ar2 compared to each other

for cov, we get non-diagonal columns equal, that's the covariance coefficient
the diagonal elements are just the (variance)^2 for each distribution
"""

#Visualsing correlation:
np.random.seed(41658165)

x = np.random.randint(low=0, high=500, size=250)
variation = np.random.normal(loc=0, scale=100, size=250) #read documentation, essentially we're generating noise

y_poscor = x + variation
y_negcor = 100 - x + variation
y_nocor = variation


def three_row_scatter(x1, y1, x2, y2, x3, y3, title1="Graph 1", title2="Graph 2", title3="Graph 3"):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))  # read documentation for more use case examples

    line1 = np.poly1d(np.polyfit(x1, y1, 1))
    line2 = np.poly1d(np.polyfit(x2, y2, 1))
    line3 = np.poly1d(np.polyfit(x3, y3, 1))

    ax1.scatter(x1, y1, marker="o", s=10)
    ax1.plot(x1, line1(x1), '-', label="Positive Relation", color="red")
    ax1.set_title(title1)

    ax2.scatter(x2, y2, marker="o", s=10)
    ax2.plot(x1, line2(x1), '-', label="Negative Relation", color="red")
    ax2.set_title(title2)

    ax3.scatter(x3, y3, marker="o", s=10)
    ax3.plot(x1, line3(x1), '-', label="No Relation", color="red")
    ax3.set_title(title3)

    plt.legend()
    plt.show()


three_row_scatter(x, y_poscor, x, y_negcor, x, y_nocor, "Positive Correlation", "Negative Correlation", "No Correlation")
cor1 = np.corrcoef(x, y_poscor)
cor2 = np.corrcoef(x, y_negcor)
cor3 = np.corrcoef(x, y_nocor)

print(str(cor1[0][1]) + "\n" + str(cor2[0][1]) + "\n" + str(cor3[0][1]) + "\n")

"""
We see a strong correlation between x and y_poscor and y_negcor, with are positive and negative respectively.
A very small value of correlation coefficient of x and y_nocor shows that there's no meaningful relation between x
and y_nocor
"""

print()
print(wholesale_data.corr())
#pairwise correlation calculator, generators a correlation matrix
