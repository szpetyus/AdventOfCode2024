import numpy as np
from tqdm import tqdm
from matplotlib import pyplot as plt
from matplotlib import animation as ani
with open("input20.txt") as ip:
    lines = np.array([list(x.strip()) for x in ip], dtype='U')

dirs = np.array([[0, 1], [-1, 0], [0, -1], [1, 0]])

track = np.zeros(lines.shape, dtype=int)
track[lines=='#'] = -1
start = np.where(lines == 'S')
start = (start[0][0], start[1][0])
end = np.where(lines == 'E')
end = (end[0][0], end[1][0])
pos = start
track[pos]=1
while pos != end:
    for d in dirs:
        if track[tuple(pos+d)] == 0:
            start_v = track[pos]
            pos = tuple(pos+d)
            track[pos] = start_v + 1
track[track>0]-=1
shortcuts = {}

part1 = 0
for start_xy, start_v in np.ndenumerate(track):
    pos = np.array(start_xy)
    if start_v >= 0:
        for d in dirs:
            dx = d*2
            tdx = tuple(pos+dx)
            if 0 <= tdx[0] < track.shape[0] and 0 <= tdx[1] < track.shape[1]:
                tp = tuple(pos)
                if track[tdx]-2 > track[tp]:
                    ps = track[tdx]-track[tp]-2
                    shortcuts[ps] = shortcuts.get(ps, 0) + 1
                    if ps >= 100:
                        part1 += 1

print("PART1", part1)

treshold = 100
part2 = 0
# test = {}
fig, ax = plt.subplots()
ims = []
for start_xy, start_v in tqdm(np.ndenumerate(track), total=track.shape[0] * track.shape[1]):
    trimg = track.copy()
    trimg[trimg > 0] = 0
    if start_v < 0:
        continue
    x0 = max(0, start_xy[1] - 21)
    y0 = max(0, start_xy[0] - 21)
    x1 = min(track.shape[0], start_xy[1] + 21)
    y1 = min(track.shape[1], start_xy[0] + 21)
    shadow_track = np.zeros(track.shape, dtype=int)-1000
    shadow_track[y0:y1, x0:x1] = track[y0:y1, x0:x1] - treshold - start_v
    pool = np.where(shadow_track >= 0)        # +distance
    for i, dest_y in enumerate(pool[0]):
        dest_x = pool[1][i]
        distance = abs(start_xy[0] - dest_y) + abs(start_xy[1] - dest_x)
        if distance <= 20 and shadow_track[dest_y,dest_x] >= distance:
            part2 += 1
            trimg[dest_y,dest_x] = 1
            # test[track[dest_y, dest_x] - start_v - distance] = test.get(track[dest_y, dest_x] - start_v - distance, 0) + 1
    if 0 < start_v < 400:
        trimg[start_xy[0], start_xy[1]] = 2
        im = ax.imshow(trimg, animated=True)
        ims.append([im])
# [print(k, v) for k, v in sorted(test.items())]
print("PART2", part2)
aa = ani.ArtistAnimation(fig, ims)
plt.show()
