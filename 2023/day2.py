lines = open("./inputs/2023/day2.txt", "r").read().splitlines() 

def part1():
    ids = 0
    for game in lines:
        id = int(game.split(":")[0].replace("Game ", ""))
        sets = game.split(": ")[1].split("; ")
        valid = True
        for subset in sets:
            red = 12
            green = 13
            blue = 14

            for move in subset.split(", "):
                amount, color = move.split(" ")
                if color == "red":
                    red -= int(amount)
                elif color == "green":
                    green -= int(amount)
                elif color == "blue":
                    blue -= int(amount)
        
            if red < 0 or green < 0 or blue < 0:
                valid = False
                break
        
        if valid:
            ids += id

    print(ids)


powers = 0
for game in lines:
    id = int(game.split(":")[0].replace("Game ", ""))
    sets = game.split(": ")[1].split("; ")
    red = 0
    green = 0
    blue = 0
    for subset in sets:
        for move in subset.split(", "):
            amount, color = move.split(" ")
            amount = int(amount)
            if color == "red" and amount > red:
                red = amount
            elif color == "green" and amount > green:
                green = amount
            elif color == "blue" and amount > blue:
                blue = amount

    powers += red * green * blue

print(powers)