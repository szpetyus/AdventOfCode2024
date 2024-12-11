from collections import deque
from time import time
with open("input11.txt") as ip:
    stones = [int(x) for x in ip.read().split(" ")]

print(stones)
sq = deque(stones)
blinks = 25
for j in range(blinks):
    # print(j, time())
    ins = deque([])
    inl = 0
    for i, s in enumerate(sq):
        ss = str(s)
        if s == 0:
            sq[i] = 1
        elif len(ss) % 2 == 0:
            ins.append((inl+i, ss[len(ss)//2:]))
            sq[i] = int(ss[:len(ss)//2])
            inl += 1
        else:
            sq[i] = s*2024
    for (i, x) in ins:
        sq.insert(i+1, int(x))
    # print(sq)
print("part 1", len(sq))

stdict = {int(x): 1 for x in stones}
blinks = 75
for j in range(blinks):
    # print(j, time())
    ins = {}
    for k in stdict:
        v = stdict[k]
        ks = str(k)
        if k == 0:
            ins[1] = ins.get(1, 0) + v
        elif len(ks) % 2 == 0:
            s1 = int(ks[len(ks)//2:])
            s2 = int(ks[:len(ks)//2])
            ins[s1] = ins.get(s1, 0) + v
            ins[s2] = ins.get(s2, 0) + v
        else:
            ins[k*2024] = ins.get(k*2024, 0) + v
    stdict = ins.copy()
    # print(sq)
print(stdict)
print("part 2", sum(stdict.values()))
