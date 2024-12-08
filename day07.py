import re
from itertools import permutations, product, combinations

with open("input07.txt") as ip:
    lines = [re.findall("(\d+)", x.strip()) for x in ip]

part1 = 0
for line in lines:
    test = int(line[0])
    test_len = len(line[2:])

    tr = {"": int(line[1])}

    for i, x in enumerate(line[2:]):
        xtr = tr.copy()
        tr = {}
        for op in xtr:
            tr[op + "+"] = xtr[op] + int(x)
            tr[op + "*"] = xtr[op] * int(x)
    if test in tr.values():
        part1 += test

    # pool = []
    # for op in ops:
    #     oop = line[1]
    #     for i, v in enumerate(line[2:]):
    #         oop = f"({oop} {op[i]} {v})"
    #     pool.append(oop)
    #
    # for x in pool:
    #     if eval(x) == test:
    #         part1 += test
    #         break
    # print(line, part1)


print(part1)

part2 = 0
for line in lines:
    test = int(line[0])
    test_len = len(line[2:])

    tr = {"": int(line[1])}

    for i, x in enumerate(line[2:]):
        xtr = tr.copy()
        tr = {}
        for op in xtr:
            tr[op + "+"] = xtr[op] + int(x)
            tr[op + "*"] = xtr[op] * int(x)
            tr[op + "||"] = int(str(xtr[op]) + x)
    if test in tr.values():
        part2 += test
print(part2)