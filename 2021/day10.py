
items = [[char for char in line] for line in open("../inputs/2021/day10.txt", "r").read().split("\n")]

mappings = {"(": ")", "[": "]", "{": "}", "<": ">"}
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
invalid_chars = []
invalid_lines = []
incomplete_lines = {}

for index, line in enumerate(items):
    current_openings = []
    for char in line:
        if char in mappings.keys():
            current_openings.append(char)
            continue
        if char != mappings[current_openings[-1]]:
            invalid_chars.append(char)
            invalid_lines.append(line)
        else:
            del current_openings[-1]

    if len(current_openings) != 0 and line not in invalid_lines:
        incomplete_lines[index] = [mappings[char] for char in current_openings]

print(sum([scores[char] for char in invalid_chars]))

for index, opens in incomplete_lines.items():
    opens.reverse()
    print(f"{items[index]} + {opens}")



#print_array([line for line in invalid_lines])
