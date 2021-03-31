import matplotlib.pyplot as plt

locations = input("Enter the locations as [L1 L2 L3 L4 ... LN]:\n")
initial_head = int(input("Enter initial head: "))
locations = [int(location) for location in locations.split(' ')]
above_head = [location for location in locations if location >= initial_head]
below_head = [location for location in locations if location < initial_head]
minimum = 0
maximum = max(locations) - (max(locations) % 10) + 10

# Creating Subplots (as two plots are to be created) ...
fig, axis = plt.subplots(1, 2)
# Setting up sub-plot attributes for plot 1
axis[0][0].title('Simulation for Upward movement')
axis[0][0].xaxis.set_tick_param(labeltop=True)
axis[0][0].xaxis.set_tick_param(labelbottom=False)
axis[0][0].yaxis.set_tick_param(labelleft=False)

# Setting up sub-plot attributes for plot 2
axis[0][1].title('Simulation for Downward movement')
axis[0][1].xaxis.set_tick_param(labeltop=True)
axis[0][1].xaxis.set_tick_param(labelbottom=False)
axis[0][1].yaxis.set_tick_param(labelleft=False)

# Working for Upward movement ...
print("For Head moving Upwards: ")
above_head.sort()
above_head.append(maximum)
below_head.sort(reverse=True)
head_track = above_head + below_head
head_movement = abs(initial_head - max(above_head)) + abs(max(above_head) - min(below_head))

# Plotting head movement ...
axis[0][0].plot(head_track, range(-1, -len(head_track) - 1, -1), '-')
axis[0][0].scatter(head_track, range(-1, -len(head_track) - 1, -1))
axis[0][0].grid()

print("The head movement for Upward simulation is", head_track)
print("The total seek time is",head_movement)

print("<------------------------------------------------------->")
# Resetting variables for downward simulation ...
above_head = [location for location in locations if location > initial_head]
below_head = [location for location in locations if location <= initial_head]

print("For Head moving Downwards: ")
below_head.sort(reverse=True)
below_head.insert(0, initial_head)
below_head.append(minimum)
head_track = below_head + above_head
head_movement = abs(initial_head - min(below_head)) + abs(min(below_head)-max(above_head))

# plotting Head Movement
axis[0][1].plot(head_track, range(-1, -len(head_track) - 1, -1), '-')
axis[0][1].scatter(head_track, range(-1, -len(head_track) - 1, -1))
axis[0][1].grid()

print("The head movement for Upward simulation is", head_track)
print("The total seek time is", head_movement)

# Showing created plots
plt.show()
