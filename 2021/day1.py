
items = [int(item) for item in open("../inputs/2021/day1.txt", "r", encoding="UTF-8").readlines()]

# --- Part One ---
print(" --- Part One ---")

print(len([item for index, item in enumerate(items) if item > items[index - 1] and index - 1 >= 0]))

# --- Part Two ---
print(" --- Part Two ---")
windows = [sum(items[index:index + 3]) for index in range(0, len(items))]
print(len([window for index, window in enumerate(windows) if window > windows[index -1] and index - 1 >= 0]))

