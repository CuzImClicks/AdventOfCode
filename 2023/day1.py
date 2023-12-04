lines = open("./inputs/2023/day1.txt", "r").read().splitlines()
sol = 0
for l in lines:
    x = ""
    for c in l:
        if c.isdigit():
            x += c
            break
    for c in l[::-1]:
        if c.isdigit():
            x += c
            break

    sol += int(x)

print(sol)
    

