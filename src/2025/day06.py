from pathlib import Path
import re
import operator as op

with open(Path(__file__).parent / '.input/day06_input') as f:
    data = f.read()

# data = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +
# """

data = data.splitlines()
ops = {'+': op.add, '*': op.mul}
input_op = [ops[str(x)] for x in re.findall(r'[+*]', data[-1])]

input = []
for line in data[:-1]:
    input.append([int(x) for x in re.findall(r'-?\d+', line)])

input1 = list(zip(*input))

def homework(inp) -> int:
    tot = 0
    for op_c, vals in zip(input_op, inp):
        ans = 1 if op_c == op.mul else 0
        for val in vals:
            ans = op_c(ans, val)
        tot += ans
    return tot

print("Part1: ", homework(input1))

input2 = [[] for _ in range(len(input_op))]

q = 0
for i_c in range(len(data[0])):
    if all([line[i_c] == " " for line in data[:-1]]):
        q += 1
        continue
    input2[q].append(int("".join([line[i_c] for line in data[:-1] if line[i_c] != " "])))


print("Part2: ", homework(input2))
