lines = open("../inputs/2022/day5.txt", "r").read().split("\n\n")[1].split("\n")

stacks = {
    "1": ['B', 'Z', 'T'],
    "2": ['V', 'H', 'T', 'D', 'N'],
    "3": ['B', 'F', 'M', 'D'],
    "4": ['T', 'J', 'G', 'W', 'V', 'Q', 'L'],
    "5": ['W', 'D', 'G', 'P', 'V', 'F', 'Q', 'M'],
    "6": ['V', 'Z', 'Q', 'G', 'H', 'F', 'S'],
    "7": ['Z', 'S', 'N', 'R', 'L', 'T', 'C', 'W'],
    "8": ['Z', 'H', 'W', 'D', 'J', 'N', 'R', 'M'],
    "9": ['M', 'Q', 'L', 'F', 'D', 'S'],
}


def part1(stacks):

    moves = []
    for line in lines:
        line = line.split(" ")
        moves.append([line[1], line[3], line[5]])

    for move in moves:
        for i in range(int(move[0])):
            char = stacks[move[1]].pop()
            stacks[move[2]].append(char)
            #print(f"Moved {char} from {move[1]} to {move[2]}")


    print("".join([f"{key}: {value}\n" for key, value in stacks.items()]))
    print("".join([stack[-1] for stack in stacks.values()]))

    # NTWZZWHFV


def part2(stacks):
    moves = []
    for line in lines:
        line = line.split(" ")
        moves.append([line[1], line[3], line[5]])

    for move in moves:
        chars = stacks[move[1]][-int(move[0]):]
        del stacks[move[1]][-int(move[0]):]
        stacks[move[2]].extend(chars)
        #print(f"Moved {chars} from {move[1]} to {move[2]}")

    print("".join([f"{key}: {value}\n" for key, value in stacks.items()]))
    print("".join([stack[-1] for stack in stacks.values()]))


part2(stacks)