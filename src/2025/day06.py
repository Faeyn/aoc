from pathlib import Path
import re
import operator as op

with open(Path(__file__).parent / '.input/day06_input') as f:
    data = f.read()

data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +
"""

data = data.splitlines()
input_op = [op.add if x == '+' else op.mul for x in re.findall(r'[+*]', data[-1])]

input1 = []
for line in data[:-1]:
    input1.append([int(x) for x in re.findall(r'-?\d+', line)])
input1 = list(zip(*input1))

q = 0
input2 = [[] for _ in range(len(input_op))]
for col in zip(*data[:-1]):
    if all([v == " " for v in col]):
        q += 1
        continue
    input2[q].append(int("".join(col)))

def homework(inp) -> int:
    tot = 0
    for op_c, vals in zip(input_op, inp):
        ans = 1 if op_c == op.mul else 0
        for val in vals:
            ans = op_c(ans, val)
        tot += ans
    return tot

print("Part1: ", homework(input1))
print("Part2: ", homework(input2))
