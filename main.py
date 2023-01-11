import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation
import pandas as pd
from itertools import count

data = pd.read_csv("ThrowingMotion.csv", header=5)

index = count()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
def getData(i):
    ax.clear()
    ax.set(xlim3d=(0, 2), xlabel='X')
    ax.set(ylim3d=(0, 2), ylabel='Y')
    ax.set(zlim3d=(0, 2), zlabel='Z')
    ax.set_title('Throwing Motion')
    i = next(index)
    for j in range(10):
        graph = ax.scatter(data['X.' + str(j + 3)][i], data['Y.' + str(j + 3)][i],
                           data['Z.' + str(j + 3)][i])


ani = matplotlib.animation.FuncAnimation(fig, getData,
                                         interval=10, blit=False)

plt.show()
