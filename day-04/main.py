import copy

bingo = open('input.txt').readlines()
bingo_numbers = bingo[0].rstrip().split(',')
bingo_boards = []
current_board = []

for line in bingo[2:]:
    if line == '\n':
        bingo_boards.append(current_board)
        current_board = []
        continue
    board_line = []
    for element in line.rstrip().split():
        board_line.append([element, False])
    current_board.append(board_line)

    if bingo.index(line) == len(bingo) - 1:
        bingo_boards.append(current_board)

def play_bingo():
    boards = copy.deepcopy(bingo_boards)
    for bingo_number in bingo_numbers:
        mark_number(bingo_number, boards)
        if bingo_numbers.index(bingo_number) >= 4:
            winning_boards = check_winning_lines(boards)
            if winning_boards != []:
                return calculate_result(bingo_number, winning_boards[0])
            winning_boards = check_winning_columns(boards)
            if winning_boards != []:
                return calculate_result(bingo_number, winning_boards[0])
    return []

def lose_bingo():
    boards = copy.deepcopy(bingo_boards)
    for bingo_number in bingo_numbers:
        mark_number(bingo_number, boards)
        if bingo_numbers.index(bingo_number) >= 4:
            winning_boards = check_winning_lines(boards)
            if winning_boards != []:
                if len(boards) > 1:
                    for winning_board in winning_boards:
                        boards.remove(winning_board)
                else:
                    return calculate_result(bingo_number, winning_boards[0])
            winning_boards = check_winning_columns(boards)
            if winning_boards != []:
                if len(boards) > 1:
                    for winning_board in winning_boards:
                        boards.remove(winning_board)
                else:
                    return calculate_result(bingo_number, winning_boards[0])
    return []

def calculate_result(bingo_number, winning_board):
    lines = [line for line in winning_board]
    unmarked_numbers = [int(pair[0]) for pairs in lines for pair in pairs if not pair[1]]
    return sum(unmarked_numbers) * int(bingo_number)

def check_winning_lines(boards):
    winning_boards = []
    for board in boards:
        for line in board:
            marked_numbers = [pair[0] for pair in line if pair[1]]
            if len(marked_numbers) == 5:
                winning_boards.append(board)
    return winning_boards

def check_winning_columns(boards):
    winning_boards = []
    for board in boards:
        for column_index in range(4):
            column = [row[column_index] for row in board]
            marked_numbers = [pair[0] for pair in column if pair[1]]
            if len(marked_numbers) == 5:
                winning_boards.append(board)
    return winning_boards

def mark_number(number, boards):
    for board in boards:
        for line in board:
            for pair in line:
                if pair[0] == number:
                    pair[1] = True

print(play_bingo())
print(lose_bingo())
