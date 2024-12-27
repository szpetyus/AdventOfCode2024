import random
from collections import deque

assert 100000000&0xffffff == 16113920
assert 12345 * 64 == 12345<<6
assert 12345 // 32 == 12345>>5
assert 12345 * 2048 == 12345<<11
assert 42 ^ 15 == 37
assert 15 ^ 42 == 37

def derive_secret(a:int) ->int:
    a = (a ^ (a << 6)) & 0xffffff
    a = (a ^ (a >> 5)) & 0xffffff
    a = (a ^ (a << 11)) & 0xffffff
    return a
    # return (((((a ^ (a << 6)) & 0xffffff) ^ (a >> 5)) & 0xffffff) ^ (a << 11)) & 0xffffff

def derive_secretN(a:int, times:int) ->int:
    for i in range(times):
        a = derive_secret(a)
    return a

def search_pattern(a:int, times:int, pattern: []) ->int:
    monkey_chart = deque([-11]*4, maxlen=4)
    hit = 0
    m = 0
    for i in range(times):
        a = derive_secret(a)
        m1 = a % 10
        monkey_chart.append(m1-m)
        if m1 - m == pattern[hit]:
            hit += 1
        else:
            hit = 0
            for j in range(4):
                if tuple(pattern[:j]) == tuple(monkey_chart)[j:]:
                    hit = j
        if hit == 4:
            return m1
        m = m1
    return 0


def identify_pattern(times: int):
    stack = deque([0xffffff]*4, maxlen=4)
    treshold = 3
    candidates = {}
    for test in range(times):
        a = random.randint(1, 0xffffff)
        hit = 0
        m = 0
        for i in range(20000):
            a = derive_secret(a)
            m1 = a % 10
            stack.append(m1-m)
            if m1 >= treshold:
                pp = tuple(stack)
                candidates[pp] = candidates.get(pp, 0) + m1
            m = m1
    top5v = sorted(candidates.values())[-5:]
    top5 = []
    for k, v in candidates.items():
        if v in top5v:
            print(k, v)
            top5.append(list(k))
    return top5


assert derive_secret(123) == 15887950, derive_secret(123)
assert derive_secret(15887950) == 16495136, derive_secret(15887950)
assert derive_secret(16495136) == 527345, derive_secret(16495136)

assert derive_secretN(1, 2000) == 8685429, derive_secret(1)

with open("input22.txt") as ip:
    lines = [derive_secretN(int(x.strip()), 2000) for x in ip]
print("PART1", sum(lines))

P = [-2, 1, -1, 3]

assert search_pattern(1, 2000, P) == 7, search_pattern(1, 2000, P)
assert search_pattern(2, 2000, P) == 7, search_pattern(2, 2000, P)
assert search_pattern(3, 2000, P) == 0, search_pattern(3, 2000, P)
assert search_pattern(2024, 2000, P) == 9, search_pattern(2024, 2000, P)

# ps = identify_pattern(30)

def identify_pattern2(times: int, tests):
    monkey_chart = deque([-11]*4, maxlen=4)
    threshold = 4
    candidates = {}
    for a in tests:
        m = 0
        for i in range(times):
            a = derive_secret(a)
            m1 = a % 10
            monkey_chart.append(m1-m)
            if m1 >= threshold:
                pp = tuple(monkey_chart)
                candidates[pp] = candidates.get(pp, 0) + m1
            m = m1
    top5v = sorted(candidates.values())[-5:]
    top5 = []
    for k, v in candidates.items():
        if v in top5v:
            print(k, v)
            top5.append(list(k))
    return top5

with open("input22.txt") as ip:
    lines = [int(x.strip()) for x in ip]
ps = identify_pattern2(2000, lines)

with open("input22.txt") as ip:
    xl = [int(x.strip()) for x in ip]

part2 = 0
for p in ps:
    with open("input22.txt") as ip:
        lines = [search_pattern(int(x.strip()), 2000, p) for x in ip]
    sl = sum(lines)
    print("TEST", p, sl)
    if sl > part2:
        part2 = sl

# 1302 too low
# 1449 someone else
# 1755 too high
# 1583 not right
# 1701 ??

print("PART2", part2)
