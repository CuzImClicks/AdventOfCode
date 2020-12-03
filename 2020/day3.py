import math


def get_trees(dx, dy) -> int:
    with open("../inputs/2020/day3.txt") as f:

        v = [x for x in f.read().splitlines()[::dy]]


    trees = 0
    x = 0
    for y in v:

        trees += (y[x % len(v[0])] == "#")
        x += dx

    return trees


to_calc = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total = []
for tup in to_calc:
    print(f"{tup[0]} | {tup[1]}")
    print(get_trees(tup[0], tup[1]))
    total.append(get_trees(tup[0], tup[1]))

print(math.prod(total))

