import numpy as np
from itertools import combinations

with open("input08.txt") as ip:
    lines = [list(x.strip()) for x in ip]

ip = np.array(lines, dtype='U')
an = np.zeros(ip.shape)

dishes = np.unique(ip)
dishes = np.delete(dishes, dishes == '.')

# print(ip)
# print(dishes)

(mapx, mapy) = ip.shape


def set_an():
    if 0 <= an1[0] < mapx and 0 <= an1[1] < mapy:
        an[an1[0], an1[1]] += 1
        return True
    return False

for d in dishes:
    pairs = list(combinations(np.rot90(np.where(ip==d)), 2))
    # print(pairs)
    for xy1, xy2 in pairs:
        d = xy2-xy1
        an1 = xy1-d
        set_an()
        an1 = xy2+d
        set_an()
        d3 = d%3
        if d3[0] == 0 and d3[1] == 0:
            an1 = xy1 + d//3
            set_an()
            an1 = xy2 - d//3
            set_an()

# print(an)
print('PART 1', np.count_nonzero(an))
an = np.zeros(ip.shape)
for d in dishes:
    pairs = list(combinations(np.rot90(np.where(ip==d)), 2))
    # print(pairs)
    for xy1, xy2 in pairs:
        d = xy2-xy1
        an1 = xy1
        set_an()
        an1 = xy2
        set_an()
        an1 = xy1 - d
        while set_an():
            an1 -= d
        an1 = xy2 + d
        while set_an():
            an1 += d
print('PART 2', np.count_nonzero(an))
