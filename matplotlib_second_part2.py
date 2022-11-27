#LOADING NECESSARY LIBRARIES
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# resize the graph

plt.figure(figsize=(6, 4), dpi=150)

#BASIC GRAPH
x_values = [0, 1, 2, 3, 4]
y_values = [0, 2, 4, 6, 8]
z_values = [0, 3, 6, 9, 12]

# makes a cool graph that is half way filled and halfway dashed(--)
x2 = np.arange(0, 4.5, 0.5)
plt.plot(x2[:5], x2[:5]**2, 'r', label = 'x values squared') # first 5 values are red and with full lines
plt.plot(x2[4:], x2[4:]**2, 'r--') # values after the fourth one are red and with dashed lines

#plt.plot(x_values, y_values, label = 'value 2x greater than x', color = 'blue', marker = 'o', markersize = 10, markeredgecolor = 'purple', markeredgewidth = 3, linewidth = 3)
#plt.plot(x_values, z_values, label = 'value 3x greater than x', color = 'red', linestyle = '--')
#plt.plot(x_values, y_values, 'y^--') # fmt = '[color][marker][line]'       there is a lot of info on markers, colors and lines in the documentation


plt.xlabel("X values", fontdict={'fontname':'Comic Sans MS'})
plt.ylabel("Y values", fontdict={'fontname':'Comic Sans MS'})
plt.title("Our First Graph", fontdict={'fontname':'Comic Sans MS', 'fontsize':'15'})

plt.xticks([0, 2, 4, 6])
#plt.yticks([0, 2, 4, 6, 7.5, 8, 10, 12, 15])

plt.legend()

plt.show()
