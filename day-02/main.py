horizontal_position = 0
depth = 0

def increase_horizontal(units):
    global horizontal_position
    horizontal_position += units

def increase_depth(units):
    global depth
    depth += units

def decrease_depth(units):
    global depth
    depth -= units

directions = {
    'forward': increase_horizontal,
    'down': increase_depth,
    'up': decrease_depth
}

commands = open('input-a.txt')

for command in commands:
    [direction, unit] = command.split(' ')
    directions[direction](int(unit))

print(horizontal_position * depth)

horizontal_position = 0
depth = 0
aim = 0

def increase_aim(units):
    global aim
    aim += units

def decrease_aim(units):
    global aim
    aim -= units

def increase_horizontal_and_depth(units):
    global horizontal_position, depth
    horizontal_position += units
    depth += aim * units

advanced_directions = {
    'forward': increase_horizontal_and_depth,
    'down': increase_aim,
    'up': decrease_aim
}

commands = open('input-b.txt')

for command in commands:
    [direction, unit] = command.split(' ')
    advanced_directions[direction](int(unit))

print(horizontal_position * depth)

