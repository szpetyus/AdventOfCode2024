import numpy as np
with open("input18.txt") as ip:
    lines = [x.strip().split(',') for x in ip]

lines=np.array(lines, dtype=int)
# print(lines)
fell = 1024
map = np.zeros((71, 71), dtype=int)
# fell = 12
# map = np.zeros((7, 7), dtype=int)
dirs = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])
pos = np.array([0,0])
dest=np.array(map.shape)


def gen_paths(map):
    alive = True
    while len(map == 0) > 0 and alive:
        alive = False
        for y in range(map.shape[0]):
            for x in range(map.shape[1]):
                if map[x, y] == 0:
                    for dx, dy in dirs:
                        x1 = x + dx
                        y1 = y + dy
                        if 0 <= x1 < map.shape[0] and 0 <= y1 < map.shape[1] and map[x1, y1] > 0:
                            alive = True
                            if map[x, y] == 0:
                                map[x, y] = map[x1, y1] + 1
                            else:
                                map[x, y] = min(map[x1, y1] + 1, map[x, y])


for i in range(fell):
    x,y = lines[i, :]
    map[x,y] = -1
map[0,0] = 1
gen_paths(map)

# print(map)
print("PART 1", map[-1,-1]-1)


fmin = 0
fmax = lines.shape[0]



while fmax-fmin>1:
    fell = (fmin+fmax) // 2

    map = np.zeros((71, 71), dtype=int)

    for i in range(fell):
        x,y = lines[i, :]
        map[x,y] = -1
    map[0,0] = 1

    for lx, ly in lines[fell:,:]:
        map[map>1] = 0
        alive = True
        map[lx,ly] = -1
        gen_paths(map)
        if fmax - fmin > 5:
            print(fmin, fmax, fell, map[-1,-1])
            if map[-1,-1] == 0:
                fmax = fell
            else:
                fmin = fell
            break
        if map[-1,-1] == 0:
            print(f"PART 2: {lx},{ly} [{map[-1,-1]-1}]")
            fmin=fmax=0
            break
# print(map)
