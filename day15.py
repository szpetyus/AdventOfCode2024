import numpy as np
from collections import deque

with open("input15.txt") as ip:
    imap = []
    imap2 = []
    mlist = ""
    iline = 0
    fpart = True
    for x in ip:
        if x == "\n":
            fpart = False
        elif fpart:
            imap.append(list(x.strip()))
            if '@' in x:
                START = np.array([x.find('@'), iline])
            x2 = x.strip().replace('#', '##').replace('.', '..').replace('O', '[]').replace('@', '@.')
            imap2.append(list(x2))
            if '@' in x:
                START2 = np.array([x2.find('@'), iline])
            iline += 1
        else:
            mlist += x.strip()

print(imap)
print(imap2)
print(mlist)
print(START)
print(START2)

md = {"<": np.array([-1, 0]), "^": np.array([0, -1]), ">": np.array([1, 0]), "v": np.array([0, 1])}

def gps(imap) ->int:
    res = 0
    for i, line in enumerate(imap):
        for j, c in enumerate(line):
            if c in 'O[':
                res += 100*i+j
            if c == '[':
                assert imap[i][j+1] == ']', (i,j)
    return res
def move_attempt(loc, mdir) -> bool:
    dest = loc + mdir
    if imap[dest[1]][dest[0]] == '.':
        imap[dest[1]][dest[0]] = imap[loc[1]][loc[0]]
        imap[loc[1]][loc[0]] = '.'
        return True
    elif imap[dest[1]][dest[0]] == '#':
        return False
    elif imap[dest[1]][dest[0]] == 'O':
        if move_attempt(dest, mdir):
            imap[dest[1]][dest[0]] = imap[loc[1]][loc[0]]
            imap[loc[1]][loc[0]] = '.'
            return True
    return False

def move_attempt2(loc, mdir, transaction: deque) -> []:
    dest = loc + mdir
    dest2 = None
    loc2 = None
    if mdir[0] == 0:
        if imap2[loc[1]][loc[0]] == '[':
            dest2 = loc + mdir + [1, 0]
            loc2 = loc + [1, 0]
        if imap2[loc[1]][loc[0]] == ']':
            dest2 = loc + mdir + [-1, 0]
            loc2 = loc + [-1, 0]
    if imap2[dest[1]][dest[0]] in '.[]':
        if [loc[0], loc[1], dest[0], dest[1], imap2[loc[1]][loc[0]]] not in transaction:
            transaction.append([loc[0], loc[1], dest[0], dest[1], imap2[loc[1]][loc[0]]])
    if dest2 is not None and imap2[dest2[1]][dest2[0]] in '.[]':
        if [loc2[0], loc2[1], dest2[0], dest2[1], imap2[loc2[1]][loc2[0]]] not in transaction:
            transaction.append([loc2[0], loc2[1], dest2[0], dest2[1], imap2[loc2[1]][loc2[0]]])
    if imap2[dest[1]][dest[0]] == '#':
        return False, None
    if dest2 is not None and imap2[dest2[1]][dest2[0]] == '#':
        return False, None
    if imap2[dest[1]][dest[0]] == ']' or imap2[dest[1]][dest[0]] == '[':
        m1, _ = move_attempt2(dest, mdir, transaction)
        if not m1:
            return False, None
    if dest2 is not None and (imap2[dest2[1]][dest2[0]] == ']' or imap2[dest2[1]][dest2[0]] == '['):
        m1, _ = move_attempt2(dest2, mdir, transaction)
        if not m1:
            return False, None
    return True, transaction

pos = START
pos2 = START2
for i, move in enumerate(mlist):
    if move_attempt(pos, md[move]):
        pos = pos + md[move]
    # if 10 <= pos2[1] <= 13 and 58 <= pos2[0] <= 62 and move == 'v':
    #     print(i)
    if i == 14693:
        print(i)
    suc, tr = move_attempt2(pos2, md[move], deque([]))
    if suc:
        for t in tr:
            imap2[t[1]][t[0]] = '.'
        while len(tr)>0:
            t = tr.pop()
            imap2[t[3]][t[2]] = t[4]
        pos2 = pos2 + md[move]

print("part1", gps(imap))
print("part2", gps(imap2))

# 1516887 too low
# print(imap2)
