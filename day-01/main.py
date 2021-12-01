depth_counter = 0
radar = open('input-a.txt')
prev_depth = int(radar.readline())

for param in radar:
    depth = int(param)
    if depth > prev_depth:
        depth_counter += 1
    prev_depth = depth

print(depth_counter)

depth_counter = 0
radar = open('input-b.txt')
params = [int(entry) for entry in radar.readlines()]
prev_depth = sum(params[0:3])

for index in range(1, len(params) - 3 + 1):
    group_depth = 0
    for group_index in range(3):
        group_depth = group_depth + params[index + group_index]
    if group_depth > prev_depth:
        depth_counter += 1
    prev_depth = group_depth

print(depth_counter)
