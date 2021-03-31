import matplotlib.pyplot as plt

locations = input("Enter the locations as [L1 L2 L3 L4 ... LN]:\n")
initial_head = int(input("Enter initial head: "))
locations = [int(location) for location in locations.split(' ')]
minimum = 0
maximum = int(input("maximum page value: "))

# Creating Subplots (as two plots are to be created) ...
fig, axis = plt.subplots(1, 2, figsize=(20, 10))
fig.suptitle("Scan Algorithm")

# Setting up sub-plot attributes for plot 1
axis[0].set_title('Upward movement')
axis[0].xaxis.set_tick_params(labeltop=True)
axis[0].xaxis.set_tick_params(labelbottom=False)
axis[0].yaxis.set_tick_params(labelleft=False)

# Setting up sub-plot attributes for plot 2
axis[1].set_title('Downward movement')
axis[1].xaxis.set_tick_params(labeltop=True)
axis[1].xaxis.set_tick_params(labelbottom=False)
axis[1].yaxis.set_tick_params(labelleft=False)

print("For Head moving Upwards: ")
above_head = [location for location in locations if location >= initial_head]
below_head = [location for location in locations if location < initial_head]
above_head.append(initial_head)
above_head.append(maximum)
below_head.append(minimum)
head_track = sorted(above_head) + sorted(below_head)
head_movement = 0
for idx, page in enumerate(head_track[:-1]):
    head_movement += abs(page - head_track[idx + 1])

print("The generated page sequence is", head_track)
print("The head movement is", head_movement)

# plotting graph
axis[0].set_xticks(range(0, maximum, 10))
axis[0].set_yticks(range(0, len(locations)+1, 1))
axis[0].plot(head_track, range(-1, -len(head_track) - 1, -1), '-')
axis[0].scatter(head_track, range(-1, -len(head_track) - 1, -1))
axis[0].grid()

print("<------------------------------------------------------------------------------------------>")
print("For head moving Downwards: ")
above_head = [location for location in locations if location >= initial_head]
below_head = [location for location in locations if location < initial_head]
below_head.append(minimum)
above_head.append(maximum)
below_head.append(initial_head)
head_track = sorted(below_head, reverse=True) + sorted(above_head, reverse=True)
head_movement = 0
for idx, page in enumerate(head_track[:-1]):
    head_movement += abs(page - head_track[idx+1])

print("The generated page sequence is", head_track)
print("The head movement is", head_movement)

# plotting graph
axis[1].set_xticks(range(0, maximum, 10))
axis[1].set_yticks(range(0, len(locations)+1, 1))
axis[1].plot(head_track, range(-1, -len(head_track) - 1, -1), '-')
axis[1].scatter(head_track, range(-1, -len(head_track) - 1, -1))
axis[1].grid()
# View Graph
plt.show()
