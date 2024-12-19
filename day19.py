from tqdm import tqdm

with open("input19.txt") as ip:
    opts = ip.readline().strip().split(', ')
    _ = ip.readline()
    lines = [x.strip() for x in ip]

# print(len(opts), len(lines))
opts = sorted(opts, key=lambda x:-len(x))

part1 = 0
part1list = []
for line in lines:
    l = line
    k = [line]
    shortlist = []
    for x, o in enumerate(opts):
        if o in line:
            shortlist.append(x)
        l = l.replace(o, str(x))
    if l.isdigit():
        part1 += 1
        part1list.append(line)
    else:
        while len(k)>0:
            kx = k.pop()
            if kx == '':
                part1 += 1
                part1list.append(line)
                break
            for o in shortlist:
                if kx.startswith(opts[o]):
                    k.append(kx[len(opts[o]):])
print("PART1", part1)

part2 = 0
for line in tqdm(part1list):
    k = {line: 1}
    shortlist = [x for x in opts if x in line]
    lo = [len(x) for x in shortlist]

    while len(k) > 0:
        rx = {}
        for kx, num in k.items():
            for i, o in enumerate(shortlist):
                if kx.startswith(o):
                    nx = kx[lo[i]:]
                    if len(nx) == 0:
                        part2 += num
                    else:
                        rx[nx] = rx.get(nx, 0) + num
        k = rx

print("PART2", part2)


