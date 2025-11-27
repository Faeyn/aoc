from collections import defaultdict, namedtuple

from advent_code.aoc_utils import get_words
from operator import and_, or_, xor

from advent_code.graph_nodes import grapher

with open('day24input') as f:
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

n_gates = [x for x in gates]
# for i, j in [(46, 59), (7, 100), (57, 90), (71, 195)]:
#     n_gates[i], n_gates[j] = n_gates[i][:-1] + n_gates[j][-1:], n_gates[j][:-1] + n_gates[i][-1:]

nodes = []
edges = []
for idx, gate in enumerate(n_gates):
    i1, i2, op, out = gate
    nodes.extend([i1, i2, out])
    edges.append((i1, out, op))
    edges.append((i2, out, op))

grapher(nodes, edges)


def gates_with_wire(wire):
    for i1, i2, op, out in gates:
        if out == wire:
            return i1, i2, op, out


def get_logic(node):
    q = [gates_with_wire(node)]
    seen = set()
    code = f"{node}"
    while q:
        i1, i2, op, out = q.pop(0)
        code = code.replace(out, f"({i1} {op} {i2})")

        if i1 not in seen:
            n_gate = gates_with_wire(i1)
            if n_gate:
                q.append(n_gate)

        if i2 not in seen:
            n_gate = gates_with_wire(i2)
            if n_gate:
                q.append(n_gate)

        seen.add(out)
    return code