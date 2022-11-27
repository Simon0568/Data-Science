#LOADING NECESSARY LIBRARIES
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


#BASIC GRAPH
x_values = [0, 1, 2, 3, 4]
y_values = [0, 2, 4, 6, 8]
z_values = [0, 3, 6, 9, 12]

plt.plot(x_values, y_values, label = 'value 2x greater than x', color = 'blue', marker = 'o', markersize = 10, markeredgecolor = 'purple', markeredgewidth = 3, linewidth = 3)
plt.plot(x_values, z_values, label = 'value 3x greater than x', color = 'red', linestyle = '--')
#plt.plot(x_values, y_values, 'y^--') # fmt = '[color][marker][line]'       there is a lot of info on markers, colors and lines in the documentation


plt.xlabel("X values", fontdict={'fontname':'Comic Sans MS'})
plt.ylabel("Y values", fontdict={'fontname':'Comic Sans MS'})
plt.title("Our First Graph", fontdict={'fontname':'Comic Sans MS', 'fontsize':'15'})

plt.xticks([0, 1, 2, 3, 4, 10])
plt.yticks([0, 2, 4, 6, 7.5, 8, 10, 12, 15])

plt.legend()

plt.show()
