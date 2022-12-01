items = open("../inputs/2021/day4.txt", "r").read().split("\n\n")

# --- Part One ---
print(" --- Part One ---")

numbers = [int(number.strip()) for number in items.pop(0).split(",")]

boards = [[[int(num) for num in line.strip().replace("  ", " ").split(" ")] for line in item.split("\n")] for item in items]

for number in numbers:
    for board in boards:
        for index, line in enumerate(board):
            if number in line:
                line[line.index(number)] = -1
                if line.count(-1) == 5 or [line[index] for line in board].count(-1) == 5:
                    #print("BINGO!")
                    #print("".join([f"{line}\n" for line in board]))
                    #print(sum([int(num) for line in board for num in line if num != " X"]) * int(number))
                    #print(number)
                    pass

# --- Part Two ---
print(" --- Part Two ---")
# https://www.reddit.com/r/adventofcode/comments/r8i1lq/comment/hp3b44g/?utm_source=share&utm_medium=web2x&context=3
exit()
boards = [[[int(num) for num in line.strip().replace("  ", " ").split(" ") if num != ""] for line in item.split("\n")] for item in items]

winners = []

for number in numbers:
    for board in boards:
        for line in board:
            if number in line:
                line[line.index(number)] = -1

        if 5 in [line.count(-1) for line in board] or 5 in [[line[i] for line in board].count(-1) for i in range(0, 5)]:
            winners.append((number, board))
            boards.remove(board)


board = winners[-1]
number = board[0]
print(number)
print("".join([f"{line}\n" for line in board[1]]))
print(f"numbers.index(number)={numbers.index(number)}/{len(numbers)}")
print(f"sum={sum([int(num) for line in board[1] for num in line if num != -1]) * int(number)}")
#
#for num in numbers:
#    for winner in winners:
#        winner = winner[1]
#        for line in winner:
#            if num in line:
#                print(f"{num}")
#                print("".join([f"{line}\n" for line in winner]))
