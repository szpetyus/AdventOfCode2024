import math

claws = []

class Cclaw:
    def __init__(self):
        self.ax = 0
        self.bx = 0
        self.ay = 0
        self.by = 0
        self.px = 0
        self.py = 0

    def __repr__(self):
        return f"claw({self.px} {self.py})"


with open("input13a.txt") as ip:
    claw = Cclaw()
    for x in ip:
        x = x.strip().replace(',', '').replace('Button ', '').replace(':', '').replace('X', '')\
            .replace('Y', '').replace('=', '').split(' ')
        if len(x) == 1:
            claw = Cclaw()
        elif x[0] == 'A':
            claw.ax = int(x[1])
            claw.ay = int(x[2])
        elif x[0] == 'B':
            claw.bx = int(x[1])
            claw.by = int(x[2])
        elif x[0] == 'Prize':
            claw.px = int(x[1])
            claw.py = int(x[2])
            claws.append(claw)

print(claws[:3])
def price(x,y):
    return x*3+y

assert price(38,86) == 200

part1 = 0
for claw in claws:
    op = []
    for a in range(claw.px//claw.ax+1):
        for b in range(claw.px//claw.bx+1):
            if a*claw.ax + b*claw.bx == claw.px:
                print(a, b, claw.px, claw.ax, claw.bx, claw.ax / claw.bx, claw.bx / claw.ax, a/b, b/a, math.gcd(claw.px, claw.ax), math.gcd(claw.px, claw.bx), math.gcd(claw.px, claw.ax * claw.bx))
                if a*claw.ay + b*claw.by == claw.py:
                    op.append((price(a, b), a, b))
    op = sorted(op)
    print(sorted(op))
    if len(op)>0:
        part1 += op[0][0]
print("part 1", part1)

EC = 10000000000000
part2 = 0
for claw in claws:
    op = []
    print(0, (claw.px)//claw.ax, (claw.px) % claw.ax, math())
    for a in range(0, (EC+claw.px)//claw.ax+1, (EC+claw.px) % claw.ax):
        for b in range(0, (EC+claw.px)//claw.bx+1, (EC+claw.px) % claw.bx):
            if a*claw.ax + b*claw.bx == EC+claw.px:
                if a*claw.ay + b*claw.by == EC+claw.py:
                    op.append((price(a, b), a, b))
    op = sorted(op)
    print(sorted(op))
    if len(op)>0:
        part2 += op[0][0]
print("part 2", part2)

