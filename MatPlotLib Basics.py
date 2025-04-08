import matplotlib.pyplot as plt
import numpy as np

x1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
y1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

x2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
y2 = (2, 4, 3, 6, 8, 7, 4, 6, 6)

#This is how we use smooth curves
x3 = np.arange(0, 9, 0.1)
y3 = np.cos(x3)

#plot function has many customisations:

#MARKER allows to add markers at every change point in the plot
#marker shape can be defined in the code, available shapes include:
# . o v ^ < > 8 s p * h H D d  P X 1 2 3 4

#to customise the LINE, we can use:
#linewidth
#linestyle

plt.plot(x1, y1, label="x=y", color="blue", marker="3", markerfacecolor="black", linewidth=1, linestyle="-.")
plt.plot(x3, abs(7 * y3), label="cosine", color="tomato", linestyle=":", linewidth="2")


#Now instead of joining the points with lines, we just want to scatter them
plt.scatter(x2, y2, color="green", marker="s", s=30)

plt.xlabel("X values")
plt.ylabel("Y values")

plt.legend()

plt.title("Plotting random things")

plt.show()
