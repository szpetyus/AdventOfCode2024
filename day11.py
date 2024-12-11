with open("input11.txt") as ip:
    stones = [int(x) for x in ip.read().split(" ")]


def blink(num_blinks, stones):
    stdict = {int(x): 1 for x in stones}
    for j in range(num_blinks):
        ins = {}
        for k in stdict:
            v = stdict[k]
            ks = str(k)
            if k == 0:
                ins[1] = ins.get(1, 0) + v
            elif len(ks) % 2 == 0:
                s1 = int(ks[len(ks) // 2:])
                s2 = int(ks[:len(ks) // 2])
                ins[s1] = ins.get(s1, 0) + v
                ins[s2] = ins.get(s2, 0) + v
            else:
                ins[k * 2024] = ins.get(k * 2024, 0) + v
        stdict = ins.copy()
        # print(sq)
    return stdict


print("part 1", sum(blink(25, stones).values()))
print("part 2", sum(blink(75, stones).values()))
