from collections import deque

def read_inputs():
    initial = {}
    outputs = {}
    op_dict = {}
    ops = deque([])
    pos = 0
    with open("input24.txt") as ip:
        for x in ip:
            if x == "\n":
                pos = 1
                continue
            if pos == 0:
                k, v = x.strip().split(": ")
                initial[k] = int(v)
            else:
                i1, op, i2, res = x.strip().replace(" -> ", " ").split(" ")
                ops.append((min(i1, i2), op, max(i1, i2), res))
                outputs[res] = (min(i1, i2), op, max(i1, i2))
                op_dict[(i1, op, i2)] = res
                op_dict[(i2, op, i1)] = res

    return initial, ops, outputs, op_dict


def eval_op(v1: bool, op: str, v2: bool) -> bool:
    if op == 'AND':
        return v1 & v2
    elif op == 'OR':
        return v1 | v2
    elif op == 'XOR':
        return v1 ^ v2


initial, ops, _, _ = read_inputs()


def exec_ops():
    part1 = 0
    X = Y = Z = 0
    while len(ops) > 0:
        i1, op, i2, res = ops.popleft()
        if i1 in initial and i2 in initial:
            x = eval_op(initial[i1], op, initial[i2])
            initial[res] = x
            if res.startswith("z"):
                bp = int(res[1:])
                if x == 1:
                    part1 |= x << bp
                else:
                    part1 &= (x << bp) ^ 0xffffffffffff
        else:
            ops.append((i1, op, i2, res))
    # print(initial, ops)
    for i in range(45):
        X |= initial[f"x{i:02}"] << i
        Y |= initial[f"y{i:02}"] << i
    return part1, X, Y, Z

part1, X, Y, Z = exec_ops()

print("part1", part1)
print(f"supposed to be {X+Y}")
print(f"{part1:048b}")
print(f"{X+Y:048b}")
print(f"{part1^(X+Y):048b}")


def findxorparent(i1, i2, op_dict):
    p0 = op_dict[(i1, 'XOR', i2)]
    for (a1, op, a2), res in op_dict.items():
        if (op == 'XOR') and (a1 == p0 or a2 == p0):
            return res
    return p0


def decompose(z, t, op_dict):
    if z in outputs:
        (i1, op, i2) = outputs[z]
        res = f"{z}=({decompose(i1, t, op_dict)} {op} {decompose(i2, t, op_dict)})"
        if i1[0] in 'xy' and int(i1[1:]) == t and op != 'XOR':
            r = findxorparent(i1, i2, op_dict)
            candidates.add((z, r, t, i1, op, i2))
        if i2[0] in 'xy' and int(i2[1:]) == t and op != 'XOR':
            r = findxorparent(i1, i2, op_dict)
            candidates.add((z, r, t, i1, op, i2))
    else:
        res = z
    return res

initial, ops, outputs, op_dict = read_inputs()
for ix in initial:
    initial[ix] = 1


candidates = set()
for z in sorted(outputs):
    if z.startswith("z"):
        print(decompose(z, int(z[1:]), op_dict))

[print(c) for c in candidates]

for a, b, _, _, _, _ in candidates:
    for i, (i1, op, i2, res) in enumerate(ops):
        if res == a:
            ops[i] = (i1, op, i2, b)
        elif res == b:
            ops[i] = (i1, op, i2, a)
    c = outputs[a]
    outputs[a] = outputs[b]
    outputs[b] = c
    co = op_dict[c]
    op_dict[outputs[a]] = op_dict[outputs[b]]
    op_dict[outputs[b]] = co

candidates = set()
for z in sorted(outputs):
    if z.startswith("z"):
        print(decompose(z, int(z[1:]), op_dict))

part1, X, Y, Z = exec_ops()
print("part1", part1)
print(f"supposed to be {X+Y}")
print(f"{part1:048b}")
print(f"{X+Y:048b}")
print(f"{part1^(X+Y):048b}")
for j, _ in enumerate(f"{part1^(X+Y):048b}"):
    if _ == '1':
        print(47-j)


def replace(i1, i2, v1, v2, v3, outputs, op_dict, part2):
    if i1 == v1 and i2 == v2:
        r1 = v3
        r2 = op_dict[(v1, 'XOR', v2)]
        ret = (min(v1, v2), max(v1, v2))
    elif i1 == v1:
        r1, r2 = i2, v2
        ret = (min(r1, v1), max(r1, v1))
    elif i1 == v2:
        r1, r2 = i2, v1
        ret = (min(r1, v2), max(r1, v2))
    elif i2 == v1:
        r1, r2 = i1, v2
        ret = (min(r1, v1), max(r1, v1))
    elif i2 == v2:
        r1, r2 = i1, v1
        ret = (min(r1, v2), max(r1, v2))
    elif i1 != v1 and i2 != v2:
        r1 = v3
        r2 = op_dict[(v1, 'XOR', v2)]
        ret = (min(v1, v2), max(v1, v2))
    else:
        raise Exception("unhandled")
    xc = outputs[r1]
    outputs[r1] = outputs[r2]
    outputs[r2] = xc
    op_dict[outputs[r1]] = r1
    op_dict[outputs[r2]] = r2
    part2.append(r1)
    part2.append(r2)
    return ret


# Znn = (a=(Xnn XOR ynn) XOR carry_n)
# carry_n = ((Xn-1 AND yn-1) OR (a-1n AND carry_n_1))

initial, ops, outputs, op_dict = read_inputs()
carry = "nvv"
part2 = []
for i in range(1, 45):
    xy1 = op_dict[(f"x{i:02}", 'XOR', f"y{i:02}")]
    pattern = f"z{i:02}=({xy1}=(x{i:02} XOR y{i:02}) XOR ({carry}={outputs[carry]}))"
    if outputs[f"z{i:02}"] == (min(xy1, carry), 'XOR', max(xy1, carry)):
        pass
        # print(pattern)
    else:
        print(pattern, "!!!", outputs[f"z{i:02}"])
        i1, op, i2 = outputs[f"z{i:02}"]
        if i1 not in [xy1, carry] or i2 not in [xy1, carry]:
            xy1, carry = replace(i1, i2, xy1, carry, f"z{i:02}", outputs, op_dict, part2)
        elif op != 'XOR':
            xy1, carry = replace(i1, i2, min(xy1, carry), max(xy1, carry), f"z{i:02}", outputs, op_dict, part2)

    c2 = op_dict[(min(xy1, carry), 'AND', max(xy1, carry))]
    c1 = op_dict[(f"x{i:02}", 'AND', f"y{i:02}")]
    carry = op_dict[min(c1, c2), 'OR', max(c1, c2)]

print("PART2", ",".join(sorted(part2)))
