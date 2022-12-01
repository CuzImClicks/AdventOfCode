items = sorted([sum([int(l) for l in line.split("\n")]) for line in open("../inputs/2022/day1.txt", "r").read().split("\n\n")], reverse=True)
print(items[0])
print(sum(sorted(items, reverse=True)[0:3]))


