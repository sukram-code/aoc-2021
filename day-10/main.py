def validate_line(line):
    opening_stack = []
    for char in line:
        if char not in chunks_map.keys():
            opening_stack.append(char)
        else:
            if chunks_map[char] != opening_stack[-1]:
                return score_map[char]
            else:
                opening_stack.pop()
    return 0

def validate_lines(lines):
    valid_lines = []
    for line in lines:
        if validate_line(line) == 0:
            valid_lines.append(line)
    return valid_lines

def calculate_line_score(line):
    score = 0
    for char in line:
        score = score * 5
        score += score_map_part2[char]
    return score

def get_closing_string(line):
    closing_string = ''
    opening_stack = []
    for char in line:
        if char in chunks_map_part2.keys():
            opening_stack.append(char)
        else:
            opening_stack.pop()
    for char in reversed(opening_stack):
        closing_string += chunks_map_part2[char]
    return closing_string

chunks_map = {
    ']': '[',
    '}': '{',
    ')': '(',
    '>': '<'
}

score_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

lines = open('input.txt').read().splitlines()

result = 0
for line in lines:
    result += validate_line(line)

print(result)

chunks_map_part2 = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

score_map_part2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

scores = []
valid_lines = validate_lines(lines)
for line in valid_lines:
    closing_string = get_closing_string(line)
    line_score = calculate_line_score(closing_string)
    scores.append(line_score)

scores.sort()
print(scores[int(len(scores)/2)])

