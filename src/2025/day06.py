from pathlib import Path
import re
import operator as op
from collections import defaultdict

with open(Path(__file__).parent / '.input/day06_input') as f:
    data = f.read()

# data = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +
# """

data = data.splitlines()
ops = {'+': op.add, '*': op.mul}

def get_nums(s: str) -> list[str]:
    return [int(x) for x in re.findall(r'-?\d+', s)]

def get_op(s: str) -> list[str]:
    return [ops[str(x)] for x in re.findall(r'[+*]', s)]

input = []
for line in data[:-1]:
    input.append(get_nums(line))

input_op = get_op(data[-1])
part_1 = 0

for i, op_c in enumerate(input_op):
    ans = 1 if op_c == op.mul else 0
    for row in input:
        ans = op_c(ans, row[i])
    part_1 += ans

print(part_1)

input2 = [defaultdict(str) for _ in range(len(input_op))]
for line in data[:-1]:
    q = 0
    v_p = "." 
    for i, v in enumerate(line):
        if v != " ":
            input2[q][i] += str(v)
        else:
            if v_p != " " and v_p != ".":
                q += 1

        v_p = v

part_2 = 0
for i_c, d in enumerate(input2):
    ans = 1 if input_op[i_c] == op.mul else 0
    for v in d.values():
        ans = input_op[i_c](ans, int(v))
    part_2 += ans

print(part_2)



