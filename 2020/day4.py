# til all() goes through all the values


passports = open("../inputs/2020/day4.txt", "r").read()
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = 0
part1 = lambda passport: all(field in passport for field in fields)
part2 = lambda entry: entry.replace("\n", " ").split(" ")


def deal_with_item(item):
    infos = []
    for index, i in enumerate(item):
        item[index] = str(i).replace("\n", "")
        for part in item[index].split(" "):
            infos.append(part)

    keys = []
    for info in infos:
        splitted = str(info).split(" ")
        for part in splitted:
            keys.append(part.split(":")[0])

    if len(keys) == 8:
        print(f"{keys} {len(keys)} {keys.index('cid')}")
        return True

    elif len(keys) == 7 and not "cid" in keys:
        print(f"{keys} {len(keys)}")
        return True


def solve(inp):
    inp = inp.split("\n\n")
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    def check1(entry):
        return all(field + ":" in entry for field in fields)

    part1 = sum(check1(x) for x in inp)

    def inrange(value, lo, hi):
        return value.isnumeric() and lo <= int(value) <= hi

    def check2(entry):
        for f in entry.replace("\n", " ").split():
            k, v = f.split(":")
            if k == "byr":
                if not inrange(v, 1920, 2002):
                    return False
            if k == "iyr":
                if not inrange(v, 2010, 2020):
                    return False
            if k == "eyr":
                if not inrange(v, 2020, 2030):
                    return False
            if k == "hgt":
                if v[-2:] not in ("cm", "in"):
                    return False
                h, u = v[:-2], v[-2:]
                if u == "cm":
                    if not inrange(h, 150, 193):
                        return False
                else:
                    if not inrange(h, 59, 76):
                        return False
            if k == "hcl":
                if v[0] != "#" or len(v) != 7 or not (set(v) <= set("0123456789abcdef#")):
                    return False
            if k == "ecl":
                if v not in "amb blu brn gry grn hzl oth".split():
                    return False
            if k == "pid":
                if not v.isnumeric() or len(v) != 9:
                    return False
        return True

    part2 = sum(check1(x) and check2(x) for x in inp)
    return part1, part2


print(solve(passports))