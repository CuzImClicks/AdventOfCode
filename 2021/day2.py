
items = [item.split(" ") for item in open("../inputs/2021/day2.txt", "r", encoding="UTF-8").readlines()]

# --- Part One ---
print(" --- Part One ---")

pos = 0 
depth = 0

for command in items:
    if command[0] == "forward":
        pos += int(command[1])
    elif command[0] == "down":
        depth += int(command[1])
    elif command[0] == "up":
        depth -= int(command[1])

print(pos * depth)

# --- Part Two ---
print(" --- Part Two ---")

pos = 0 
depth = 0
aim = 0

for command in items:
    if command[0] == "forward":
        pos += int(command[1])
        depth += aim * int(command[1])
    elif command[0] == "down":
        #depth += int(command[1])
        aim += int(command[1])
    elif command[0] == "up":
        #depth -= int(command[1])
        aim -= int(command[1])

print(pos * depth)
