import math

items = open("../inputs/2020/day5.txt", "r").readlines()

calculate_seat_id = lambda row, seat: row * 8 + seat


def solve(item):
    letters = [char for char in item]
    rows = letters[:-3]
    seats = list(item[-3:])

    row = 0
    turn = 1
    for letter in rows:

        if letter == "F":
            row += 0
            turn += 1

        elif letter == "B":
            if turn == 1:
                row += 64
                turn += 1

            elif turn == 2:
                row += 32
                turn += 1

            elif turn == 3:
                row += 16
                turn += 1

            elif turn == 4:
                row += 8
                turn += 1

            elif turn == 5:
                row += 4
                turn += 1

            elif turn == 6:
                row += 2
                turn += 1

            elif turn == 7:
                row += 1
                turn += 1

    turn_seats = 1
    seat = 0
    for char in seats:
        if char == "L":
            turn_seats += 1

        elif char == "R":
            if turn_seats == 1:
                seat += 4
                turn_seats += 1

            elif turn_seats == 2:
                seat += 2
                turn_seats += 1

            elif turn_seats == 3:
                seat += 1
                turn_seats += 1

    return calculate_seat_id(row, seat)


seat_ids = []

for item in items:
    item = item.replace("\n", "")

    seat_ids.append(solve(item))

sorted_ids = sorted(seat_ids)

for index, entry in enumerate(sorted_ids):
    try:
        if int(sorted_ids[index]) + 1 == int(sorted_ids[index + 1]) - 1:
            print(sorted_ids[index] + 1)

    except IndexError:
        pass


