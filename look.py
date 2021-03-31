import matplotlib.pyplot as plt

locations = input("Enter the locations as [L1 L2 L3 L4 ... LN]:\n")
initial_head = int(input("Enter initial head: "))
locations = [int(location) for location in locations.split(' ')]
above_head = [location for location in locations if location >= initial_head]
below_head = [location for location in locations if location < initial_head]
minimum = 0
maximum = int(input("Maximum page value: "))

# Creating Subplots (as two plots are to be created) ...
fig, axis = plt.subplots(1, 2, figsize=(20, 15))
fig.suptitle("LOOK Algorithm")

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

# Working for Upward movement ...
print("For Head moving Upwards: ")
above_head.append(initial_head)
above_head.sort()
below_head.sort(reverse=True)
head_track = above_head + below_head
track_moment = 0
for idx, track in enumerate(head_track[:-1]):
    track_moment += abs(track - head_track[idx+1])

# Plotting head movement ...
axis[0].set_xticks(range(0, maximum, 10))
axis[0].set_yticks(range(0, len(locations)+1, 1))
axis[0].plot(head_track, range(-1, -len(head_track) - 1, -1), '-')
axis[0].scatter(head_track, range(-1, -len(head_track) - 1, -1))
axis[0].grid()

print("The head movement for Upward simulation is", head_track)
print("The total seek time is", track_moment)

print("<------------------------------------------------------->")
# Resetting variables for downward simulation ...
above_head = [location for location in locations if location > initial_head]
below_head = [location for location in locations if location <= initial_head]

print("For Head moving Downwards: ")
below_head.sort(reverse=True)
below_head.insert(0, initial_head)
head_track = below_head + above_head
track_moment = 0
for idx, track in enumerate(head_track[:-1]):
    track_moment += abs(track - head_track[idx+1])

# plotting Head Movement
axis[1].set_xticks(range(0, maximum, 10))
axis[1].set_yticks(range(0, len(locations)+1, 1))
axis[1].plot(head_track, range(-1, -len(head_track) - 1, -1), '-')
axis[1].scatter(head_track, range(-1, -len(head_track) - 1, -1))
axis[1].grid()

print("The head movement for Upward simulation is", head_track)
print("The total seek time is", track_moment)

# Showing created plots
plt.show()
