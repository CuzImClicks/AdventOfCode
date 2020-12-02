items = open("D:/GitHub Repos/AdventOfCode/inputs/2015/day2.txt", "r").read().splitlines()
total = 0
for item in items:
    w, h, l = item.split("x")
    w, h, l = int(w), int(h), int(l)
    wrap = 2*min(w+h, w+l, l+h)
    bow = w * h * l
    total += wrap + bow

print(total)

