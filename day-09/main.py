data = open('input.txt').read().splitlines()
heights = []
for line in data:
    heights.append([int(c) for c in line])
columns = len(heights[0])
rows = len(heights)

corners = [(0, 0), (0, columns - 1), (rows - 1, 0), (rows - 1, columns - 1)]
sides = []
top_bottom = []

for i in range(1, columns):
    top_bottom.append((0, i))
    top_bottom.append((rows - 1, i))

for i in range(1, rows):
    sides.append((i, 0))
    sides.append((i, columns - 1))

def check_corner(x, y):
    value = heights[x][y]
    y_to_check = [0, 1] if y == 0 else [columns - 1, columns - 2]
    if (x == 0):
        if (heights[x + 1][y_to_check[0]] > value and heights[x][y_to_check[1]] > value):
            return value + 1
    else:
        if (heights[x - 1][y_to_check[0]] > value and heights[x][y_to_check[1]] > value):
            return value + 1
    return 0

def check_side(x, y):
    value = heights[x][y]
    y_to_check = [0, 1] if y == 0 else [columns - 1, columns - 2]
    if (heights[x + 1][y_to_check[0]] > value and heights[x - 1][y_to_check[0]] > value and heights[x][y_to_check[1]] > value):
        return value + 1
    return 0

def check_top_bottom(x, y):
    value = heights[x][y]
    other_x = x + 1 if x == 0 else x - 1
    if (heights[x][y - 1] > value and heights[x][y + 1] > value and heights[other_x][y] > value):
        return value + 1
    return 0

def check_four_sides(x, y):
    value = heights[x][y]
    if (heights[x - 1][y] > value and heights[x + 1][y] > value and heights[x][y - 1] > value and heights[x][y + 1] > value):
        return value + 1
    return 0

low_points = 0
for i in range(rows):
    for j in range(columns):
        if (i, j) in corners:
            low_points += check_corner(i, j)
        elif (i, j) in sides:
            low_points += check_side(i, j)
        elif (i, j) in top_bottom:
            low_points += check_top_bottom(i, j)
        else:
            low_points += check_four_sides(i, j)

print(low_points)
