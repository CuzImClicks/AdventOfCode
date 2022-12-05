def pretty_string(item):
    return [
        "".join(
            ["-" if number in range(item[0][0], item[0][1]) else " " for number in range(0, 101)]) + "\n",
        "".join(["-" if number in range(item[1][0], item[1][1]) else "  " for number in range(0, 101)])
    ]


def part1():
    items = [[[int(part) for part in element.split("-")] for element in line.split(",")] for line in
             open("../inputs/2022/day4.txt").read().splitlines()]
    item = items[0]
    print("".join([str(number) if number in range(item[0][0], item[0][1]) else "." for number in range(0, 101)]))
    print("".join([str(number) if number in range(item[1][0], item[1][1]) else "." for number in range(0, 101)]))

    items = [line for line in items
             if (line[1][0] >= line[0][0] and line[1][1] <= line[0][1]) or (
                     line[1][0] <= line[0][0] and line[1][1] >= line[0][1])]

    for item in items:
        print(item[1][0] >= item[1][0] and item[1][1] <= item[1][1])  #
        print(item[1][0] <= item[0][0] and item[1][1] >= item[0][1])  #
        print("".join(pretty_string(item)))
        print("\n")

    # print_array(items)
    print(len(items))


def part2():
    items = [[[int(part) for part in element.split("-")] for element in line.split(",")] for line in
             open("../inputs/2022/day4.txt").read().splitlines()]

    overlap = [line for line in items
               if (line[0][1] >= line[1][0] >= line[0][0])
               or (line[1][1] >= line[0][0] >= line[1][0])]

    removed = [item for item in items if item not in overlap]
    for line in overlap:
        print()
        print("".join(pretty_string(line)))
        print("\n")

    print(len(overlap))
