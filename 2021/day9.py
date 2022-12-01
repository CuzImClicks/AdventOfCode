
lines = [[int(char) for char in line] for line in open("../inputs/2021/day9.txt", "r").read().split("\n")]

low_points = []
for index_line, line in enumerate(lines):
    for index_point, point in enumerate(line):
        if index_line - 1 >= 0:
            if lines[index_line - 1][index_point] <= point:
                continue
        if index_point - 1 >= 0:
            if line[index_point - 1] <= point:
                continue
        if index_point + 1 <= len(line) - 1:
            if line[index_point + 1] <= point:
                continue
        if index_line + 1 <= len(lines) - 1:
            if lines[index_line + 1][index_point] <= point:
                continue

        print(f"{index_point}|{index_line} -> {point}")
        low_points.append(point + 1)

print(sum(low_points))
