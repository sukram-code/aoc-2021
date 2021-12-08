SEGMENTS_TO_LOOK = [2, 4, 3, 7]

data_lines = open('input.txt').read().splitlines()
counter = 0

for line in data_lines:
    output_entry = line.split(' | ')[1]
    for number in output_entry.split():
        if len(number) in SEGMENTS_TO_LOOK:
            counter += 1

print(counter)
