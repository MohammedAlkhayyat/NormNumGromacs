import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# load the data from the CSV file
data = []
with open("my_file.csv") as f:
    for line in f:
        x, y, z, c = map(float, line.split(","))
        data.append((x, y, z, c))

# create a figure and a 3D Axes
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# scatter plot
x, y, z, c = zip(*data)
ax.scatter(x, y, z, c=c, cmap="RdYlBu")

# line plot
for i in range(len(x)):
    for j in range(i+1, len(x)):
        if (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2 <= 0.6 ** 2:
            ax.plot([x[i], x[j]], [y[i], y[j]], [z[i], z[j]], color="k")

plt.show()
