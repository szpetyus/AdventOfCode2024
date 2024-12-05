import regex

with open("input03.txt") as ip:
    ram = ip.read()

# ram = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

mulsr = regex.findall("mul\((\d{1,3}),(\d{1,3})\)", ram)
part1 = 0
print(mulsr)
for x, y in mulsr:
    part1 += int(x) * int(y)

# not 30243322
print("part 1", part1)

mulsr = regex.findall("(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))",
              "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
print(mulsr)

mulsr = regex.findall("(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))",
              ram)

part2 = 0
mul = True
for cmd, x, y in mulsr:
    if cmd == "do()":
        mul = True
    elif cmd == "don't()":
        mul = False
    elif cmd.startswith("mul") and mul:
        part2 += int(x) * int(y)
print("part 2", part2)
