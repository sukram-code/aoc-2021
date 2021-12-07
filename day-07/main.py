import sys

crabs = [int(crab) for crab in open('input.txt').read().splitlines()[0].split(',')]

unique_positions = []

for i in range(min(crabs), max(crabs) + 1):
    unique_positions.append(i)

min_fuel = sys.maxsize

for position in unique_positions:
    fuel_amount = 0
    for crab in crabs:
        fuel_amount += abs(position - crab)
    if fuel_amount < min_fuel:
        min_fuel = fuel_amount

print(min_fuel)

min_fuel = sys.maxsize

for position in unique_positions:
    fuel_amount = 0
    for crab in crabs:
        distance = abs(position - crab)
        fuel_amount += int(distance * (distance + 1) / 2)
    if fuel_amount < min_fuel:
        min_fuel = fuel_amount

print(min_fuel)
