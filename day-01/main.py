depth_counter = 0
radar = open('input-a.txt')
prev_depth = int(radar.readline())

for param in radar:
    depth = int(param)
    if depth > prev_depth:
        depth_counter += 1
    prev_depth = depth

print(depth_counter)

