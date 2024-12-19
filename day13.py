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


claws = []
with open("input13.txt") as ip:
    claw = Cclaw()
    for x in ip:
        x = x.strip().replace(',', '').replace('Button ', '').replace(':', '').replace('X', '') \
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


def price(x3, y1):
    return x3 * 3 + y1


assert price(38, 86) == 200

for p, EC in enumerate([0, 10000000000000]):
    part = 0
    for claw in claws:
        op = []
        py = EC + claw.py
        px = EC + claw.px

        a = (py * claw.bx - px * claw.by) / (claw.bx * claw.ay - claw.ax * claw.by)
        b = (px - a * claw.ax) / claw.bx
        if a == int(a) and b == int(b) and a > 0 and b > 0:
            part += price(a, b)

    print(f"part {p + 1}: {int(part)}")

# next year comment:
# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400 -> [80,40]
# import numpy as np
# np.linalg.solve(np.array([[94, 22],[34, 67]]), np.array([8400,5400])) -> [80,40]

