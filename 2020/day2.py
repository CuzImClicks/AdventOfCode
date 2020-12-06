
items = open("D:/GitHub Repos/AdventOfCode/inputs/2020/day2.txt", "r").read().splitlines()

valid = 0
total = 0
for line in items:

    pwd = line.split(" ")
    if len(pwd) == 0:
        pass
    elif len(pwd) == 3:
        amount = pwd[0].split("-")
        letter = pwd[1][0]
        word = pwd[2]
        letters = {}
        total += 1

        for let in word:
            if not let in letters:
                letters[let] = 1

            else:
                letters[let] += 1

        value = letters.get(letter)

        if value:
            if int(value) >= int(amount[0]):
                if int(value) <= int(amount[1]):
                    valid += 1
                    print(f"{valid} - {letter} - {len(word)} - {amount[0]}:{amount[1]} - {letters[letter]}")
