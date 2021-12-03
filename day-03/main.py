diagnostics = open('input.txt')
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

def search_for_oxygen_rating(bit_arr, pos):
    if len(bit_arr) == 1:
        return ''.join(bit_arr[0])

    count_zeroes = 0
    count_ones = 0
    for row in range(len(bit_arr)):
        if bit_arr[row][pos] == '1':
            count_ones += 1
        else:
            count_zeroes += 1
    if count_ones >= count_zeroes:
        return search_for_oxygen_rating([bit for bit in bit_arr if bit[pos] == '1'], pos + 1)
    else:
        return search_for_oxygen_rating([bit for bit in bit_arr if bit[pos] == '0'], pos + 1)

def search_for_co2_rating(bit_arr, pos):
    if len(bit_arr) == 1:
        return ''.join(bit_arr[0])

    count_zeroes = 0
    count_ones = 0
    for row in range(len(bit_arr)):
        if bit_arr[row][pos] == '1':
            count_ones += 1
        else:
            count_zeroes += 1
    if count_ones >= count_zeroes:
        filtered_bits = [bit for bit in bit_arr if bit[pos] == '0']
        return search_for_co2_rating(filtered_bits, pos + 1)
    else:
        filtered_bits = [bit for bit in bit_arr if bit[pos] == '1']
        return search_for_co2_rating(filtered_bits, pos + 1)

oxygen_rating = search_for_oxygen_rating(bits, 0)
co2_rating = search_for_co2_rating(bits, 0)

print(int(oxygen_rating, 2) * int(co2_rating, 2))
