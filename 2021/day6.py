
items = [int(num) for num in open("../inputs/2021/day6.txt", "r").read().split(",")]
#
#for _ in range(0, 81):
#    zeros = items.count(0)
#    items = [fish - 1 if fish != 0 else 6 for fish in items]
#    for _ in range(0, zeros):
#        items.append(8)
#
#print(len(items))

#items = [3,4,3,1,2]

for i in range(0, 256):
    zeros = items.count(0)
    items = [fish - 1 if fish != 0 else 6 for fish in items]
    print(f"After {i} days: {len(items)}")
    for _ in range(0, zeros):
        items.append(8)


print(len(items))
