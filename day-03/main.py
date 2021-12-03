diagnostics = open('input-a.txt')
bits = [list(diagnostic.rstrip()) for diagnostic in diagnostics.readlines()]

rows = len(bits)
columns = len(bits[0])

gamma = ''
epsilon = ''

for column in range(columns):
    count_zeroes = 0
    count_ones = 0
    for row in range(rows):
        if bits[row][column] == '1':
            count_ones += 1
        else:
            count_zeroes += 1
    if count_zeroes > count_ones:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(int(gamma, 2) * int(epsilon, 2))
