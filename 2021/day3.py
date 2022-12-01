
from collections import Counter

items = [list(item.strip().replace("\n", "")) for item in open("../inputs/2021/day3.txt", "r", encoding="UTF-8").readlines()]

# --- Part One ---
print(" --- Part One ---")

bits = [[num[i] for num in items] for i in range(0, len(items[0]))]
common_bits = ["0" if bit.count("0") >= len(bit) // 2 else "1" for bit in bits]
least_bits = ["0" if bit.count("0") < len(bit) // 2 else "1" for bit in bits]

print(int("".join(common_bits), 2) * int("".join(least_bits), 2))

# --- Part Two ---
print(" --- Part Two ---")

#oxygen = [[num for num in items if num[i] == common_bits[i]] for i in range(0, len(items[0]))]
#fitting = items
#for i in range(0, len(items[0])):
#    common_bits = ["0" if bit.count("0") >= len(bit) // 2 else "1" for bit in fitting]
#    fitting = [num for num in items if num[i] == common_bits[i]]
#print(len(fitting))

theta = ""
epsilon = ""
for i in range(len(items[0])):
    common = Counter([x[i] for x in items])
    
    
items = [list(item.strip().replace("\n", "")) for item in open("../inputs/2021/day3.txt", "r", encoding="UTF-8").readlines()]
    
for i in range(len(items[0])):
    common = Counter(x[i] for x in items)
    if common["0"] > common["1"]:
        items = [x for x in items if x[i] == "1"]
    else:
        items = [x for x in items if x[i] == "0"]
    if items:
        epsilon = items[0]
        
print(int(theta, 2)*int(epsilon,2))



