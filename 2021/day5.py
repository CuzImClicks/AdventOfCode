class Line:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2} "


items = [[[int(num.strip()) for num in part.split(",")] for part in line.split(" -> ")] for line in
         open("../inputs/2021/day5.txt", "r").readlines()]
items = [vec for vec in items if vec[0][0] == vec[1][0] or vec[0][1] == vec[1][1]]
items = [Line(vec[0][0], vec[0][1], vec[1][0], vec[1][1]) for vec in items]

plane = [[[0 for _ in range(0, 1001)] for _ in range(0, 1001)] for _ in range(0, 1001)]

for line in items:
    if line.x1 == line.x2:
        i = line.y1
        while i != line.y2:
            plane[1][i] += 1
            if line.y1 >= line.y2:
                i -= 1
            else:
                i += 1

    elif line.y1 == line.y2:
        i = line.x1
        while i != line.x2:
            plane[0][i] += 1
            if line.x1 >= line.x2:
                i -= 1
            else:
                i += 1

print([])
