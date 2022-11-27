from matplotlib import pyplot as plt

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
hours = []
print(range(0, 8, 1))
for day in days:
    hours.append(int(input(f"Enter the amount of hours for the day {day}: ")))
  
plt.title("Phone Usage", fontdict={'fontname':'Comic Sans MS', 'fontsize':'30'})
plt.plot([1, 2, 3, 4, 5, 6, 7], hours, 'rh--')
plt.xlabel("Days of the week", fontdict={'fontname':'Comic Sans MS', 'fontsize':'15'})
plt.ylabel("Hours", fontdict={'fontname':'Comic Sans MS', 'fontsize':'15'})

plt.show()

