chars = [char for char in open("../inputs/2022/day6.txt", "r").read()]


def part1():
    for index, char in enumerate(chars[:-4]):
        print(chars[index:index + 4])
        test = len(set(chars[index:index + 4])) == 4
        if test:
            print(f"{index + 4} {test}")
            break


def part2():
    for index, char in enumerate(chars[:-14]):
        print(chars[index:index + 14])
        test = len(set(chars[index:index + 14])) == 14
        if test:
            print(f"{index + 14} {test}")
            break
