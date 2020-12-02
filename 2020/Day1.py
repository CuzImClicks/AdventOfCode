
items = open("D:/GitHub Repos/AdventOfCode/inputs/2020/day1.txt", "r").read().split(",")


def one(first, second):
    amount = int(first) + int(second)
    if amount == 2020:
        print(f"{first} + {second} = {amount}")
        two(first, second)


def two(first, second):
    print(f"{first} * {second} = {first*second}")


for item in items:

    for item2 in items:
        one(int(item), int(item2))






