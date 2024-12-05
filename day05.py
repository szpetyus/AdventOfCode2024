before = {}
after = {}
updates = []
split = False
with open("input05.txt") as ip:
    for x in ip:
        if split:
            updates.append(x.strip().split(","))
        else:
            if x == "\n":
                split = True
            else:
                ab = x.strip().split("|")
                a = ab[0]
                b = ab[1]
                if b in before:
                    before[b].append(a)
                else:
                    before[b] = [a]
                if a in after:
                    after[a].append(b)
                else:
                    after[a] = [b]

part1 = 0
part2 = 0

# print(after)
# print(before)
# print(updates)
unordered = []

for i in updates:
    ordered = True
    assert len(i) & 1 == 1, "nem páratlan"
    middle = len(i)//2
    # print(len(i), middle)
    for j in range(len(i)-1):
        for k in range(j+1, len(i)):
            if i[k] in after and i[j] in after[i[k]]:
                ordered = False
            if i[j] in before and i[k] in before[i[j]]:
                ordered = False
    if ordered:
        # print("OK", i, i[middle])
        part1 += int(i[middle])
    else:
        unordered.append(i)

print(part1)

for i in unordered:
    ordered = True
    middle = len(i)//2
    for j in range(len(i)-1):
        for k in range(j+1, len(i)):
            if i[k] in after and i[j] in after[i[k]]:
                c = i[j]
                i[j] = i[k]
                i[k] = c
            if i[j] in before and i[k] in before[i[j]]:
                c = i[j]
                i[j] = i[k]
                i[k] = c
    part2 += int(i[middle])
print(part2)

