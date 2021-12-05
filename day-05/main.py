class VentLine:

    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x = int(start_x)
        self.start_y = int(start_y)
        self.end_x = int(end_x)
        self.end_y = int(end_y)

    def is_diagonal(self):
        return abs(self.start_x - self.end_x) == abs(self.start_y - self.end_y)

    def __str__(self):
        return f'{self.start_x},{self.start_y} -> {self.end_x},{self.end_y}'

    def __repr__(self):
        return str(self)

def mark_horizontal(start_x, end_x, y, field):
    for index in range(min([start_x, end_x]), max([start_x, end_x]) + 1):
        field[y][index] += 1

def mark_vertical(start_y, end_y, x, field):
    for index in range(min([start_y, end_y]), max([start_y, end_y]) + 1):
        field[index][x] += 1

def mark_diagonal(vent_line, field):
    x = vent_line.start_x
    y = vent_line.start_y
    x_end = vent_line.end_x + 1 if vent_line.end_x >  vent_line.start_x else vent_line.end_x - 1
    y_end = vent_line.end_y + 1 if vent_line.end_y >  vent_line.start_y else vent_line.end_y - 1
    while (x, y) != (x_end, y_end):
        field[y][x] += 1
        if x < x_end:
            x += 1
        else:
            x -= 1
        if y < y_end:
            y += 1
        else:
            y -= 1

vents_data = open('input.txt').read().splitlines()
vent_lines = []

for data_entry in vents_data:
    coords = data_entry.split(' -> ')
    start = coords[0]
    end = coords[1]
    vent_lines.append(VentLine(start.split(',')[0], start.split(',')[1], end.split(',')[0], end.split(',')[1]))

max_x_start = max([vent.start_x for vent in vent_lines])
max_x_end = max([vent.end_x for vent in vent_lines])
max_y_start = max([vent.start_y for vent in vent_lines])
max_y_end = max([vent.end_y for vent in vent_lines])
max_coord = max([max_x_start, max_x_end, max_y_start, max_y_end])

field = []
field2 = []
field_line = [0 for i in range(max_coord + 1)]
for i in range(max_coord + 1):
    field.append(list(field_line))
    field2.append(list(field_line))

for vent_line in vent_lines:
    if vent_line.start_x != vent_line.end_x and vent_line.start_y != vent_line.end_y:
        continue
    if vent_line.start_x == vent_line.end_x:
        mark_vertical(vent_line.start_y, vent_line.end_y, vent_line.start_x, field)
    else:
        mark_horizontal(vent_line.start_x, vent_line.end_x, vent_line.start_y, field)

overlapping_points = [point for lines in field for point in lines if point > 1]
print(len(overlapping_points))

for vent_line in vent_lines:
    if vent_line.is_diagonal():
        mark_diagonal(vent_line, field2)
    elif vent_line.start_x == vent_line.end_x:
        mark_vertical(vent_line.start_y, vent_line.end_y, vent_line.start_x, field2)
    elif vent_line.start_y == vent_line.end_y:
        mark_horizontal(vent_line.start_x, vent_line.end_x, vent_line.start_y, field2)
    else:
        print(f'skipping {vent_line}')

overlapping_points = [point for lines in field2 for point in lines if point > 1]
print(len(overlapping_points))
