valid_pwd = 0

for i in range(206938, 679128):
    word = str(i)
    prev = 0
    valid = True
    double = False
    for char in word:

        one, two, three, four, five, six = [char for char in word]
        if one <= two <= three <= four <= five <= six:
            valid = True
            if one == two:
                double = True
            if two == three:
                double = True
            if three == four:
                double = True
            if four == five:
                double = True
            if five == six:
                double = True
    if valid and double:
        valid_pwd += 1

print(valid_pwd)







