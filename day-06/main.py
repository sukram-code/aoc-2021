DAYS_PART1 = 80
DAYS_PART2 = 256
MATURE_FISH_TIMER = 6
YOUNG_FISH_TIMER = 8

def fresh_count():
    result = {}
    for i in range(9):
        result[i] = 0
    return result

def count_fishes(start_population, days):
    for day in range(days):
        reset_fishes = start_population.pop(0)
        population = fresh_count()
        for key, value in start_population.items():
            population[key - 1] = value
        population[MATURE_FISH_TIMER] += reset_fishes
        population[YOUNG_FISH_TIMER] += reset_fishes
        start_population = population
    return sum(value for key, value in start_population.items())

fishes = [int(fish) for fish in open('input.txt').read().splitlines()[0].split(',')]

fish_and_count = fresh_count()

for fish in fishes:
    fish_and_count[fish] += 1

print(count_fishes(dict(fish_and_count), DAYS_PART1))
print(count_fishes(dict(fish_and_count), DAYS_PART2))

