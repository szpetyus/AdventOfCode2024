import numpy as np
with open("input09.txt") as ip:
    x = ip.read().strip()

disk = np.zeros(100000, dtype=int)
loc = 0
for i, v in enumerate(list(x)):
    if i % 2 == 0:
        disk[loc:loc+int(v)] = i//2
    else:
        disk[loc:loc+int(v)] = -1
    loc += int(v)
assert (loc,) < disk.shape, f"MIN {loc}"
disk = np.resize(disk, loc)
disk2 = disk.copy()
loc -= 1
assert disk[loc] != -1

end = loc
for i in range(loc):
    if disk[i] == -1:
        while disk[end] == -1 and end > i:
            end -= 1
        disk[i] = disk[end]
        disk[end] = -1
        end -= 1
    if end <= i:
        break

checksum = 0
for i in range(loc):
    if disk[i] == -1:
        break
    checksum += i * disk[i]

print(i, disk[i-3:i+3])

# not 6607239990971
# its 6607511583593
print("PART 1", checksum)


def findmove(id, flen, pos):
    st = -1
    for j in range(pos+1):
        if disk2[j] == -1:
            if st == -1:
                st = j
            if st != -1 and flen-1 == j-st:
                # print("--",  disk2[st-1:j+2], disk2[pos:pos+flen+2])
                disk2[st:j+1] = id
                disk2[pos+1:pos+flen+1] = -1
                # print("++", disk2[st-1:j+2], disk2[pos:pos+flen+2])
                return
        else:
            st = -1


end = loc
f = -1
flen = 0
print(disk2)
for i in range(end, 0, -1):
    if i % 10000 == 0: print("...sector ", i)
    if disk2[i] == -1 and f == -1:
        pass
    elif f == disk2[i]:
        flen += 1
    elif f != disk2[i]:
        if f != -1:
            findmove(f, flen, i)
        f = disk2[i]
        flen = 1

checksum = 0
for i in range(loc):
    if disk2[i] != -1:
        checksum += i * disk2[i]

print(disk2)

# 6636608910639 too high
print("PART 2", checksum)
