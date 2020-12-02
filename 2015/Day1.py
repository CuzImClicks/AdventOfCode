items = open("D:/GitHub Repos/AdventOfCode/inputs/2015/day1.txt", "r").read()

word = []
floor = 0

for item in [char for char in items]:

    if floor == -1:
        break

    word.append(item)

    if item == "(":
        floor += 1

    if item == ")":
        floor -= 1

print(len(word))
