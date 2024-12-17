with open("input17.txt") as ip:
    lines = [x.strip().split(": ") for x in ip]

ops = ['0', '1', '2', '3', 'A', 'B', 'C']
ints = {
    '0': "A=A//(2**op)",
    '1': "B=B^op",
    '2': "B=op & 7",
    '3': "IP=op if A>0 else IP",
    '4': "B=B^C",
    '5': "print(f'{op & 7},', end='')",
    '6': "B=A//(2**op)",
    '7': "C=A//(2**op)"}


# A = (((((0*8+2)*8+1)*8+6)*8+1)*8+6) ->  2 5 2 5 3
# A = (((((((((0*8+2)*8+1)*8+6)*8+2)*8+1)*8+6)*8+2)*8+1)*8+6) ->  2 5 3 2 5 3 2 5 3
# A = (((((((((((0*8+2)*8+9)*8+8)*8+7)*8+6)*8+5)*8+4)*8+3)*8+2)*8+1)*8+0)*8+2 ->  3,1,5,7,0,3,2,7,7,2,7,0
# A = ((((((((3*8+3)*8+3)*8+2)*8+2)*8+2)*8+1)*8+1)*8+1) -> 3,3,5,3,3,7,0,0,0
# A = ((3*8+3)*8+3) -> 0,0,0,
# A = ((((7*8+7)*8+7)*8+7)*8+7) -> 0,0,0,4,7,
# A = 7 --> 7
A = int(lines[0][1])
B = int(lines[1][1])
C = int(lines[2][1])
IP = 0
prog = lines[-1][1].split(',')
print(lines, A, B, C, prog)

print("PART 1: ", end="")
while IP < len(prog):
    cmd = ints[prog[IP]].replace('op', ops[int(prog[IP+1])])
    IP += 2
    exec(cmd)
    # print(cmd, f"A:{A}, B:{B}, C:{C}, IP:{IP}")

print()
IP = 0

class runit():
    def __init__(self, lines, Ax):
        self.res = ""
        self.IP = self.B = self.C = self.A = 0
        self.A = Ax
        self.prog = lines[-1][1].split(',')
        self.ops = ['0', '1', '2', '3', 'self.A', 'self.B', 'self.C']
        self.ints = {
            '0': "self.A=self.A//(2**op)",
            '1': "self.B=self.B^op",
            '2': "self.B=op & 7",
            '3': "self.IP=op if self.A>0 else self.IP",
            '4': "self.B=self.B^self.C",
            '5': "self.res += f'{op & 7},'",
            '6': "self.B=self.A//(2**op)",
            '7': "self.C=self.A//(2**op)"}

    def calc(self):
        while self.IP < len(self.prog):
            cmd = self.ints[self.prog[self.IP]].replace('op', self.ops[int(self.prog[self.IP + 1])])
            self.IP += 2
            exec(cmd)
            # print(cmd, f"A:{self.A}, B:{self.B}, C:{self.C}, IP:{self.IP}")
        return self.res[:-1]

x = runit(lines, int(lines[0][1]))
print('PART 1', x.calc())
x = runit(lines, (((((+3)*8+0)*8+4)*8+5)*8+1))
print('3,5,5,3,0:', x.calc())

# AINIT = 0
# searchrange = 7
# i = len(prog)-1
# while i >= 0:
#     target = prog[i]
#     print(">", i, target, end=" ")
#     found = False
#     for j in range(searchrange,-searchrange,-1):
#         x = runit(lines, AINIT * 8 + j)
#         xc = x.calc()
#         if i< 1 and xc.startswith('2,4,1,'):
#             print("!!!!!!!", xc, j, j%8, A, B, C)
#         if lines[-1][1].endswith(xc):
#             print("---", j, xc, "---",  lines[-1][1][i*2:])
#         if lines[-1][1].endswith(xc):
#             AINIT = AINIT * 8 + j
#             print(":", j)
#             found = True
#             break
#         pass
#     if not found:
#         searchrange = (searchrange+1)*64
#         print(f"range {searchrange} -{searchrange}", end=" ")
#     else:
#         searchrange = 6
#         i = i-1


# print(AINIT)
# x = runit(lines, AINIT)
# xc = x.calc()
# print(xc, "--", lines[-1][1])
# assert xc == lines[-1][1], (xc, "--", lines[-1][1])
# print("PART 2", AINIT)
A = 0
# for i in range(15):
#     pass
# for j in range(8**4):
#     # A = j
#     # A = 2557+j*8**4
#     """
#     xc: 2,4,1,3,7,5,5 1546749
#     xc: 2,4,1,3,7,5,5,3 5741053
#     xc: 2,4,1,3,7,5,5,4 9935357
#     xc: 2,4,1,3,7,5,5,6 14129661
#     """
#     # A = 5741053+j*8**4
#     # 18323965 14 3072 2,4,1,3,7,5,4,1,1 ['2', '4', '1', '3', '7', '5', '4', '1', '1', '3', '0', '3', '5', '5', '3', '0']
#     # A = 18323965 + j * 8 ** 8
#     # 20419418621 14 1216 2,4,1,3,7,5,4,1,1,3,0,3 ['2', '4', '1', '3', '7', '5', '4', '1', '1', '3', '0', '3', '5', '5', '3', '0']
#     # A = 20419418621 + j*8**12
#     """
#     9641146161661 14 140 2,4,1,3,7,5,4,1,1,3,0,3,5,5,3 ['2', '4', '1', '3', '7', '5', '4', '1', '1', '3', '0', '3', '5', '5', '3', '0']
#     11565291510269 14 168 2,4,1,3,7,5,4,1,1,3,0,3,5,5,3 ['2', '4', '1', '3', '7', '5', '4', '1', '1', '3', '0', '3', '5', '5', '3', '0']
#     11840169417213 14 172 2,4,1,3,7,5,4,1,1,3,0,3,5,5,3 ['2', '4', '1', '3', '7', '5', '4', '1', '1', '3', '0', '3', '5', '5', '3', '0']
#     """
#     A = 9641146161661 + j*8**12
#     x = runit(lines, A)
#     xc = x.calc()
#     if xc.startswith(lines[-1][1][:31]):
#         print("xc:", xc, A)
#     if lines[-1][1].startswith(xc):
#         print(A, j, xc, prog)
# print(A, xc)
a_base = [0]
for expo in range(15):
    b_base = set()
    for base in a_base:
        for j in range(8**4):
            A = base + j*8**expo
            x = runit(lines, A)
            xc = x.calc()
            # if xc.startswith(lines[-1][1][:expo*2+4]):
            #     print("xc:", xc, A)
            if lines[-1][1].startswith(xc[:-2]):
                # print(A, j, xc, prog)
                b_base.add(A)
            if xc == lines[-1][1]:
                print("Early stop", xc, "Part2:", A)
                break
        if xc == lines[-1][1]:
            break
    if xc == lines[-1][1]:
        break
    a_base = b_base.copy()
    print(a_base)
# xc: 2,4,1,3,7,5,4,1,1,3,0,3,5,5,3,0 108107566389757

for A in a_base:
    x = runit(lines, A)
    xc = x.calc()
    if xc == lines[-1][1]:
        print("THIS", xc, "Part2:", A)
        break
