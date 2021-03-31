import matplotlib.pyplot as plt
head_movement = 0
locations = input("Enter the locations in disks as [L1 L2 L3 L4 ... L5]: \n")
locations = [int(location) for location in locations.split(' ') if location.isdigit()]


for idx, loc in enumerate(locations[:-1]):
    head_movement += abs(loc-locations[idx+1])

print("The total Head Movement is", head_movement)

fig, axes = plt.subplots(1, 1, figsize=(5, 5))
fig.suptitle('FCFS Scheduling')
axes.xaxis.set_tick_params(labeltop=True)
axes.xaxis.set_tick_params(labelbottom=False)
axes.yaxis.set_tick_params(labelleft=False)
axes.plot(locations, range(-1, -len(locations)-1, -1), '-')
axes.scatter(locations, range(-1, -len(locations)-1, -1))
axes.grid()
plt.xticks(range(0, max(locations)+11, 10), fontsize=10)
plt.yticks(fontsize=10)
for y, x in enumerate(locations):
    plt.text(x+0.02, -y-1+.02, str(x))

plt.show()