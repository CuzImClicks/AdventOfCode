items = open("../inputs/2021/day4.txt", "r").read().split("\n\n")

# --- Part One ---
print(" --- Part One ---")

numbers = items.pop(0).split(",")

boards = [[line.replace("  ", " ").split(" ") for line in item.split("\n")] for item in items]

for number in numbers:
    for board in boards:
        for index, line in enumerate(board):
            if number in line:
                line[line.index(number)] = " X"
                if line.count(" X") == 5 or [line[index] for line in board].count(" X") == 5:
                    print("BINGO!")
                    print("".join([f"{line}\n" for line in board]))
                    print(sum([int(num) for line in board for num in line if num != " X"]) * int(number))
                    print(number)
                    exit()
                    pass

# --- Part One ---
print(" --- Part Two ---")

boards = [[[num for num in line.replace("  ", " ").split(" ") if num != ""] for line in item.split("\n")] for item in
          items]

winners = []

for number in numbers:
    for board in boards:
        for index, line in enumerate(board):
            if number in line:
                line[line.index(number)] = " X"

        if 5 in [[line[i] for line in board].count(" X") for i in range(0, 5)] or 5 in [[line[i] for line in board].count(" X") for i in range(0, 5)]:
            winners.append((number, board))
            boards.remove(board)
        #    if len(boards) == 0:
#
        #        print("".join([f"{line}\n" for line in board]))
        #        print(len(winners))
        #        print(sum([int(num) for line in board for num in line if num != " X"]) * int(number))
#
