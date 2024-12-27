import numpy as np
from itertools import permutations, product
# from functools import cache


with open("input21.txt") as ip:
    lines = [x.strip() for x in ip]

keypad = [  "+---+---+---+",
            "| 7 | 8 | 9 |",
            "+---+---+---+",
            "| 4 | 5 | 6 |",
            "+---+---+---+",
            "| 1 | 2 | 3 |",
            "+---+---+---+",
            "    | 0 | A |",
            "    +---+---+"]

arrowpad = ["    +---+---+",
            "    | ^ | A |",
            "+---+---+---+",
            "| < | v | > |",
            "+---+---+---+"]

keys = {}
for R, r in enumerate(keypad):
    for C, c in enumerate(r):
        if c in "0123456789A":
            keys[c] = (R, C)
arrows = {}
for R, r in enumerate(arrowpad):
    for C, c in enumerate(r):
        if c in "<>v^A":
            arrows[c] = (R, C)

keys["avoid"] = (keys['A'][0], keys['1'][1])
arrows["avoid"] = (arrows['A'][0], arrows['<'][1])
# THIS ORDER IS CRITCAL for PART1
dirs = {(0, -4): '<', (2, 0): 'v', (0, 4): '>', (-2, 0): '^', }
# /THIS ORDER IS CRITCAL for PART1
dirs2 = {v: k for k, v in dirs.items()}
stepcache = {}


def is_good_dir(dest, pos, dir):
    (desty, destx) = dest
    (posy, posx) = pos
    (diry, dirx) = dir
    if posy-desty > 0:
        if 0 <= posy-desty+diry < posy-desty:
            return True
    elif posy-desty < 0:
        if 0 >= posy-desty+diry > posy-desty:
            return True
    if posx-destx > 0:
        if 0 <= posx-destx+dirx < posx-destx:
            return True
    elif posx-destx < 0:
        if 0 >= posx-destx+dirx > posx-destx:
            return True
    return False

# @lru_cache(maxsize=2048)
def robot_push(sequence, aperture_name):
    aperture = eval(aperture_name)
    global stepcache
    sp = ""
    (posy, posx) = aperture['A']
    step_from = 'A'
    for x in sequence:
        (desty, destx) = aperture[x]
        if (step_from, x) in stepcache:
            sp += stepcache[(step_from, x)]
            posy = desty
            posx = destx
        else:
            step = ""
            for avoid_void in range(2):
                for d in dirs:
                    pos_reset = (posy, posx)
                    sp_reset = sp
                    step_reset = ""
                    while is_good_dir((desty, destx), (posy, posx), d):
                        posx += d[1]
                        posy += d[0]
                        sp += dirs[d]
                        step += dirs[d]
                        if aperture["avoid"] == (posy, posx):
                            (posy, posx) = pos_reset
                            sp = sp_reset
                            step = step_reset
                            break
            stepcache[(step_from, x)] = step+'A'
            sp += 'A'
        step_from = x
    return sp


assert robot_push("029A", "keys") == "<A^A>^^AvvvA", (robot_push("029A", "keys"), "<A^A>^^AvvvA")
assert int("029A"[:-1]) == 29

# print(robot_push(robot_push(robot_push("029A", "keys"), "arrows"), "arrows"))
# print(len(robot_push(robot_push(robot_push("029A", "keys"), "arrows"), "arrows")))
# print(lines, keys, arrows)

testcase = {
    "029A": "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
    "980A": "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A",
    "179A": "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
    "456A": "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A",
    "379A": "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
}

for x in testcase:
    assert len(robot_push(robot_push(robot_push(x, "keys"), "arrows"), "arrows")) == len(testcase[x]), (
        robot_push(robot_push(robot_push(x, "keys"), "arrows"), "arrows"), testcase[x])

part1 = 0
for l in lines:
    part1 += len(robot_push(robot_push(robot_push(l, "keys"), "arrows"), "arrows")) * int(l[:-1])
print("PART1", part1)
assert part1==156714


part2 = 0
all_legit_path = {k: set() for k in (product('1234567890A', repeat=2))}
all_legit_path |= {k: set() for k in (product('<>v^A', repeat=2))}

avoid = []
for move, p in all_legit_path.items():
    aperture = keys if move[0] in keys and move[1] in keys else arrows
    (posy, posx) = aperture[move[0]]
    (desty, destx) = aperture[move[1]]
    step = ""
    for d in dirs:
        while is_good_dir((desty, destx), (posy, posx), d):
            posx += d[1]
            posy += d[0]
            step += dirs[d]
    p = set(permutations(step))
    all_legit_path[move] = p

    for i, step in enumerate(p):
        if len(step)>2 and ((step[0] == step[2] and step[0] != step[1]) or (step[-1] == step[-3] and step[-2] != step[-1])):
            avoid.append((move, step))
            # break
        pos = aperture[move[0]]
        for j in step:

            pos = tuple(np.array(pos) + np.array(dirs2[j]))
            if pos == aperture['avoid']:
                avoid.append((move, step))
                # print("avoid", move, step)
                # break
for move, step in avoid:
    all_legit_path[move].discard(step)

# @cache
def shortest_path(begin, end, depth):
    res = 1<<64-1
    if begin is None:
        begin = 'A'
    if (begin, end, depth) in shortest_path_cache:
        return shortest_path_cache[(begin, end, depth)]
    # print(f"[{begin}:{end}::", end="")
    candidates = all_legit_path[(begin, end)]
    for steps in candidates:
        asteps = list(steps)+['A']
        l = 0
        last = None
        for s in asteps:
            if depth > 0:
                l += shortest_path(last, s, depth-1)
            else:
                l += 1
                # print(s, end="")
            last = s
        if l < res:
            res = l
    # print(f"({res})]", end="")
    shortest_path_cache[(begin, end, depth)] = res
    return res

shortest_path_cache = {}

def seq(buttons, depth):
    res = 0
    last = None
    for b in buttons:
        res += shortest_path(last, b, depth)
        last = b
    return res

print("\n 029A:", seq('029A', 2), "\n")

for x in testcase:
    assert seq(x, 2) == len(testcase[x]), (seq(x, 2), len(testcase[x]), testcase[x])

part1a = 0
for l in lines:
    part1a += seq(l, 2) * int(l[:-1])
print("PART1 controll", part1a)
assert part1a == part1

part2 = 0
for l in lines:
    part2 += seq(l, 25) * int(l[:-1])
print("PART2", part2)
