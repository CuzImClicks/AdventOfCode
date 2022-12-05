
items = open("../inputs/2022/day3.txt", "r").read().splitlines()

score = 0

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for char in chars:
    #print(char, chars.index(char) + 1)
    pass

for line in items:
    #print(line)
    first = line[:len(line) // 2]
    second = line[len(line) // 2:]
    #print(first, second)
    for char in first:
        if char in second:
            score += chars.index(char) + 1
            break

#print(score)

# Part Two

def split(l, n):

    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

items = list(split(items, 3))

score = 0

for group in items:
    for char in group[0]:
        if char in group[1] and char in group[2]:
            score += chars.index(char) + 1
            break

print(score)
