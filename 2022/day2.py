
#couldnt solve
# print(*map(sum,zip(*[(b-87+3*((b-a-67)%3),1+(b-88)*3+(a+b-151)%3)for l in open('input.txt').readlines()if(a:=ord(l[0]),b:=ord(l[2]))])))

inp = [line for line in open("../inputs/2022/day2.txt", "r").read().split("\n")]

# A, X = Rock = 1
# B, Y = Paper = 2
# C, Z = Scissors = 3

points = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

scores = {
    "X": 0,
    "Y": 3,
    "Z": 6,
    "A": 1,
    "B": 2,
    "C": 3,
}

print(sum([points[play] for play in inp]))

score = 0

for enemy, outcome in [line.split(" ") for line in inp]:
    score += scores[outcome]
    if outcome == "Y":
        score += scores[enemy]
        
    elif outcome == "X":
        score += scores[]
