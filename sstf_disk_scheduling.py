import matplotlib.pyplot as plt

locations = input("Enter the locations in disks as [L1 L2 L3 L4 ... L5]: \n")
head = int(input("Enter initial head position: "))
minimum = 0
locations = [int(location) for location in locations.split(' ') if location.isdigit()]
maximum = max(locations) - (max(locations)%10) + 10
final_sequence = [head]
head_movement = 0

while True:
    if len(locations) == 0:
        break

    displacement_from_head = sorted([(location,abs(location-head)) for location in locations], key=lambda x:x[1])[0]
    head = displacement_from_head[0]
    head_movement += displacement_from_head[1]
    locations.remove(head)
    final_sequence.append(head)

print("The order of movement of head: ", final_sequence)

fig, axes = plt.subplots()
axes.xaxis.set_tick_params(labeltop=True)
axes.xaxis.set_tick_params(labelbottom=False)
axes.yaxis.set_tick_params(labelleft=False)
plt.title('SSTF Scheduling')
axes.plot(final_sequence, range(-1, -len(final_sequence)-1, -1), '-')
axes.scatter(final_sequence, range(-1, -len(final_sequence)-1, -1))
axes.grid()

plt.xticks(range(0, max(final_sequence)+11, 10), fontsize=10)
plt.yticks(range(-1, -len(final_sequence)-1, -1), fontsize=10)

for y, x in enumerate(final_sequence):
    plt.text(x+0.02, -y-1+0.02, str(x))

plt.show()