with open("input04.txt") as ip:
    lines = [x.strip() for x in ip]

def wchk(key, lines, x0, y0, xi, yi):
    x = x0
    y = y0
    for i in key:
        if len(lines[0]) > x >= 0 and len(lines) > y >= 0:
            if lines[y][x] != i:
                return 0
        else:
            return 0
        x += xi
        y += yi
    return 1

def wchk4(lines, x0, y0):
    res = 0
    for a in range(-1, 2):
        for b in range(-1, 2):
            res += wchk('XMAS', lines, x0, y0, a, b)
    return res

def wchk2(lines, x0, y0):
    res = 0
    if lines[y0][x0] == 'A':
        for a in range(-1, 2, 2):
            for b in range(-1, 2, 2):
                res += wchk('MAS', lines, x0-a, y0-b, a, b)
        if res == 2:
            return 1
    return 0


part1 = 0
part2 = 0
for y0 in range(len(lines)):
    for x0 in range(len(lines[0])):
        part1 += wchk4(lines, x0, y0)
        part2 += wchk2(lines, x0, y0)

print(part1)
print(part2)

