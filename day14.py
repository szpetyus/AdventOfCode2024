from tqdm import tqdm
import numpy as np
from matplotlib import animation, collections, patches
from matplotlib import pyplot as plt

with open("input14.txt") as ip:
    lines = [x.strip().replace('p=', '').replace('v=', '').replace(',', ' ').split(' ') for x in ip]

# print(lines)
area = (101, 103)
# area = (11, 7)
steps = 100

def botmove(bot, steps, area, zones, mz):
    res = bot.copy()
    res[0] = (int(bot[0]) + int(bot[2]) * steps) % area[0]
    res[1] = (int(bot[1]) + int(bot[3]) * steps) % area[1]
    res.append(-1)
    if res[0] in zones[0] and res[1] in zones[2]:
        res[4] = 1
        mz[0] += 1
    elif res[0] in zones[0] and res[1] in zones[3]:
        res[4] = 3
        mz[2] += 1
    if res[0] in zones[1] and res[1] in zones[2]:
        res[4] = 2
        mz[1] += 1
    elif res[0] in zones[1] and res[1] in zones[3]:
        res[4] = 4
        mz[3] += 1
    if res[4] == -1:
        pass
    return res

def botmove2(bot, area):
    bot[0] = (int(bot[0]) + int(bot[2])) % area[0]
    bot[1] = (int(bot[1]) + int(bot[3])) % area[1]
    return (bot[0], bot[1])


sx = area[0]//2
sy = area[1]//2
zones = [range(0, sx), range(area[0]-sx, area[0]+1), range(0, sy), range(area[1]-sy, area[1]+1)]
mz = [0,0,0,0]
p1bots = [botmove(bot, 100, area, zones, mz) for bot in lines]
# print(mz)
part1 = 1
for x in mz:
    part1 *= x
print("part 1", part1)
# print(list(range(0, sx)), list(range(area[0]+1-sx, area[0]+1)), list(range(0, sy)), list(range(area[1]+1-sy, area[1]+1)))

# print(p1bots)


t = 0
tf = 0
canvas, axes = plt.subplots()
canvas.set_dpi(50)
axes.set_xlim(0, area[0])
axes.set_ylim(0, area[1])
# print(np.array(lines, dtype=int)[:, :2])
dots = collections.PatchCollection([patches.Circle((int(x[0]), int(x[1])), radius=1.0) for x in lines])
axes.add_collection(dots)
frame_text = axes.text(0.05, 0.95,'',horizontalalignment='left',verticalalignment='top', transform=axes.transAxes)
def upd_f(frame_no):
    dots.set_paths([patches.Circle(botmove(bot, frame_no, area, zones, mz), radius=1.0) for bot in lines])
    frame_text.set_text(f"FRAME: {frame_no}    ")

ani = animation.FuncAnimation(fig=canvas, func=upd_f, frames=tqdm(range(6390, 6399)), interval=500.0)
ani.save("day14.gif")

# for frame in tqdm(range(1, 20000)):
#     p2bots = np.array([botmove2(bot, area) for bot in lines], dtype=int)
#     center_col = np.count_nonzero(np.logical_and(p2bots[:,0] <= area[0]//2+10, p2bots[:,0] >= area[0]//2-15))
#     if center_col == t:
#         print(f"early stop? {center_col} {tf} {frame}")
#     if center_col > t:
#         t = center_col
#         tf = frame
# print("max center col", t, "@ frame ", tf)
