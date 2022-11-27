from matplotlib import pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [5, 3, 1, 4, 2]

x2_values = [1, 2, 3, 4, 5]
y2_values = [1, 2, 5, 4, 7]

plt.plot(x_values, y_values, color="red")
plt.scatter(x2_values, y2_values, color="blue")

plt.title("Basic Data Chart")

plt.xlabel("X values")
plt.ylabel("Y values")


plt.show()