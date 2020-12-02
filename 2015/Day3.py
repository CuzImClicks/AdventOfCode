count = 0
items = open("D:/GitHub Repos/AdventOfCode/inputs/2015/day3.txt", "r").read()
items = [char for char in items]
coords = {}
global coord
coord = {"x": 0, "y": 0}

for item in items:
    count += 1
    print("\rMoves: " + str(count), end="")

    if item == "^":
        coord["y"] += 1

    elif item == ">":
        coord["x"] += 1

    elif item == "v":
        coord["y"] -= 1

    elif item == "<":
        coord["x"] -= 1

    if not str(coord) in coords:
        coords[str(coord)] = 1

    else:
        coords[str(coord)] += 1

print("\nTotal houses with at least one present: " + str(len(coords)))