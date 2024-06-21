import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Absentees_data = pd.read_csv("Absenteeism_at_work.csv", sep=r'\s*;\s*', engine='python')
#sep=r'\s*;\s*' is used to define the separators used in the csv file, specific for each file

x = Absentees_data["Age"]
y = Absentees_data["Distance from Residence to Work"]

fig, axs = plt.subplots(figsize=(12, 6))
axs.hist(Absentees_data["Month of absence"], bins=12, color="yellow", rwidth=.8)

plt.title("Absences by month")
plt.xlabel("Months")
plt.show()

#data = Absentees_data.groupby(["Month of absence"]).mean()

#data = data["Absenteeism time in hours"]
#data.plot(kind="line")

#plt.show()
