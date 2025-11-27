from collections import defaultdict

from advent_code.aoc_utils import get_words
from operator import and_, or_, xor

with open('day24input_max') as f:
    data = f.read()

p1, p2 = data.split("\n\n")
p1 = p1.splitlines()
p2 = p2.splitlines()

wire_start_value = {}
for line in p1:
    wire, value = line.split(": ")
    wire_start_value[wire] = int(value)

op_map = {'AND': and_, 'OR': or_, 'XOR': xor}

gates = []
for line in p2:
    input_wire1, operator_name, input_wire2, output_wire = get_words(line)
    gates.append((input_wire1, input_wire2, operator_name, output_wire))


def solve_values(wire_start, gates):
    w = {k: v for k, v in wire_start.items()}
    g = [x for x in gates]
    while g:
        c_len = len(g)
        for _ in range(c_len):
            i1, i2, op_name, o = g.pop(0)
            if i1 in w and i2 in w:
                w[o] = op_map[op_name](w[i1], w[i2])
            else:
                g.append((i1, i2, op_name, o))
        if c_len == len(g):
            return None
    return w


def get_val(letter, wires):
    bin = []
    for k, v in sorted(wires.items(), key=lambda x: x[0]):
        if k.startswith(letter):
            bin.append(str(v))
    return ''.join(reversed(bin))


for i in range(45):
    wires_0 = {k: 0 if k.startswith('y') or k.startswith('x') else v for k, v in wire_start_value.items()}
    wires_0[f'y{"{:02}".format(i)}'] = 1
    wires_0[f'x{"{:02}".format(i)}'] = 1
    print(get_val('z', solve_values(wires_0, gates)), i)


# l_g = len(gates)
# for i in range(l_g):
#     for j in range(i + 1, l_g):
#         n_gates = [x for x in gates]
#         n_gates[i], n_gates[j] = n_gates[i][:-1] + n_gates[j][-1:], n_gates[j][:-1] + n_gates[i][-1:]
#
#         wires_0 = {k: 0 if k.startswith('y') or k.startswith('x') else v for k, v in wire_start_value.items()}
#         wires_0[f'x36'] = 1
#         wires_0[f'y36'] = 1
#         solved_wires_0 = solve_values(wires_0, n_gates)
#
#         if solved_wires_0 is None:
#             continue
#
#         z = get_val('z', solved_wires_0)
#         if bin(z) == "0b10000000000000000000000000000000000000":
#             print(i, j)
#

#
# for p1 in [(1, 59), (36, 59), (46, 59), (51, 59), (59, 156)]:
#     for p2 in [(7, 100), (42, 100), (100, 177)]:
#         for p3 in [(25, 185), (29, 185), (43, 90), (43, 125), (43, 185), (57, 90), (57, 125), (57, 185)]:
#             for p4 in [(71, 93), (71, 195), (93, 161), (99, 161), (161, 166), (161, 180), (161, 195)]:
#
#                 n_gates = [x for x in gates]
#                 for i, j in [p1, p2, p3, p4]:
#                     n_gates[i], n_gates[j] = n_gates[i][:-1] + n_gates[j][-1:], n_gates[j][:-1] + n_gates[i][-1:]
#
#                 w_solved = solve_values(wire_start_value, n_gates)
#                 z = get_val('z', w_solved)
#                 y = get_val('y', w_solved)
#                 x = get_val('x', w_solved)
#
#                 correct_sol = True
#                 correct_sol = correct_sol and y + x == z
#
#                 if not correct_sol:
#                     continue
#
#                 answer_key = '0b10'
#                 for i1 in range(45):
#                     w = {k: 0 if k.startswith('y') or k.startswith('x') else v for k, v in wire_start_value.items()}
#                     w[f'x{"{:02}".format(i1)}'] = 1
#                     w[f'y{"{:02}".format(i1)}'] = 1
#                     w_solved = solve_values(w, n_gates)
#                     z = get_val('z', w_solved)
#                     correct_sol = correct_sol and bin(z) == answer_key
#                     answer_key += '0'
#
#                 if not correct_sol:
#                     continue
#
#                 answer_key = '0b1'
#                 for i1 in range(45):
#                     w = {k: 0 if k.startswith('y') or k.startswith('x') else v for k, v in wire_start_value.items()}
#                     w[f'x{"{:02}".format(i1)}'] = 1
#                     w[f'y{"{:02}".format(i1)}'] = 0
#                     w_solved = solve_values(w, n_gates)
#                     z = get_val('z', w_solved)
#                     correct_sol = correct_sol and bin(z) == answer_key
#                     answer_key += '0'
#
#                 if not correct_sol:
#                     continue
#
#                 answer_key = '0b1'
#                 for i1 in range(45):
#                     w = {k: 0 if k.startswith('y') or k.startswith('x') else v for k, v in wire_start_value.items()}
#                     w[f'x{"{:02}".format(i1)}'] = 0
#                     w[f'y{"{:02}".format(i1)}'] = 1
#                     w_solved = solve_values(w, n_gates)
#                     z = get_val('z', w_solved)
#                     correct_sol = correct_sol and bin(z) == answer_key
#                     answer_key += '0'
#
#                 if not correct_sol:
#                     continue
#
#                 answer_key = '0b110'
#                 for i1 in range(45):
#                     w = {k: 0 if k.startswith('y') or k.startswith('x') else v for k, v in wire_start_value.items()}
#                     w[f'x{"{:02}".format(i1)}'] = 1
#                     w[f'y{"{:02}".format(i1)}'] = 1
#                     w[f'x{"{:02}".format(i1+1)}'] = 1
#                     w[f'y{"{:02}".format(i1+1)}'] = 1
#                     w_solved = solve_values(w, n_gates)
#                     z = get_val('z', w_solved)
#                     correct_sol = correct_sol and bin(z) == answer_key
#                     answer_key += '0'
#
#                 if not correct_sol:
#                     continue
#
#                 answer_key = '0b100'
#                 for i1 in range(45):
#                     w = {k: 0 if k.startswith('y') or k.startswith('x') else v for k, v in wire_start_value.items()}
#                     w[f'x{"{:02}".format(i1)}'] = 1
#                     w[f'y{"{:02}".format(i1)}'] = 1
#                     w[f'x{"{:02}".format(i1+1)}'] = 0
#                     w[f'y{"{:02}".format(i1+1)}'] = 1
#                     w_solved = solve_values(w, n_gates)
#                     z = get_val('z', w_solved)
#                     correct_sol = correct_sol and bin(z) == answer_key
#                     answer_key += '0'
#
#                 if not correct_sol:
#                     continue
#
#                 answer_key = '0b100'
#                 for i1 in range(45):
#                     w = {k: 0 if k.startswith('y') or k.startswith('x') else v for k, v in wire_start_value.items()}
#                     w[f'x{"{:02}".format(i1)}'] = 1
#                     w[f'y{"{:02}".format(i1)}'] = 1
#                     w[f'x{"{:02}".format(i1+1)}'] = 1
#                     w[f'y{"{:02}".format(i1+1)}'] = 0
#                     w_solved = solve_values(w, n_gates)
#                     z = get_val('z', w_solved)
#                     correct_sol = correct_sol and bin(z) == answer_key
#                     answer_key += '0'
#
#                 if not correct_sol:
#                     continue
#
#                 answer_key = '0b11'
#                 for i1 in range(45):
#                     w = {k: 0 if k.startswith('y') or k.startswith('x') else v for k, v in wire_start_value.items()}
#                     w[f'x{"{:02}".format(i1)}'] = 1
#                     w[f'y{"{:02}".format(i1)}'] = 0
#                     w[f'x{"{:02}".format(i1+1)}'] = 1
#                     w[f'y{"{:02}".format(i1+1)}'] = 0
#                     w_solved = solve_values(w, n_gates)
#                     z = get_val('z', w_solved)
#                     correct_sol = correct_sol and bin(z) == answer_key
#                     answer_key += '0'
#
#                 if not correct_sol:
#                     continue
#
#                 if correct_sol:
#                     print(p1, p2, p3, p4)
#
#
# def print_ans(ls):
#     ans = []
#     for p1, p2 in ls:
#         ans.append(gates[p1][-1])
#         ans.append(gates[p2][-1])
#
#     print(",".join(sorted(ans)))
#
#
# print_ans([(36, 59), (7, 100), (57, 90), (71, 195)])
# print_ans([(36, 59), (7, 100), (57, 185), (71, 195)])
# print_ans([(46, 59), (7, 100), (57, 90), (71, 195)])
# print_ans([(36, 59), (7, 100), (57, 185), (71, 195)])
