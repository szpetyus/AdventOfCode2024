with open("input02.txt") as ip:
    lines = [x.strip().split(" ") for x in ip]

d = []
safe = []
unsafe = []


def is_safe(testline):
    s = True
    z = []
    for j in range(len(testline) - 1):
        d0 = int(testline[j]) - int(testline[j + 1])
        if d0 == 0 or d0 < -3 or d0 > 3:
            s = False
        if s and len(z) > 0 and z[-1] * d0 < 0:
            s = False
        else:
            z.append(d0)
    return s, z


for l in lines:
    s, z = is_safe(l)

    d.append(z)
    if s == 1:
        safe.append(l)
    else:
        unsafe.append(l)

print("part 1", len(safe))
# print(unsafe)

safe2 = []
unsafe2 = []
for l in unsafe:
    is_safe2 = False
    for i2 in range(len(l)):
        line = l.copy()
        drop = line.pop(i2)
        is_safe2, z = is_safe(line)
        if is_safe2:
            break
    if is_safe2:
        safe2.append(l)
    else:
        unsafe2.append(l)
# print(z, skip, s)
# ! 643, 648, 656, 641
print(unsafe2)

print("part 2", len(safe)+len(safe2))

