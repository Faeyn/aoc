import operator
from collections import defaultdict
from copy import deepcopy
from pprint import pprint

import numpy as np
from icecream import ic
import re

with open('day19_input') as f:
    data = f.read().splitlines()

rules = defaultdict(list)
split_rules = defaultdict(list)

parts = []

op_map = {"<": operator.lt, ">": operator.gt}
opp_op_map = {">": operator.le, "<": operator.ge}

input_for_parts = False
for row_d in data:
    if input_for_parts and row_d:
        parts.append(eval(f'dict({row_d.replace("{", "").replace("}", "")})'))
    elif not input_for_parts and row_d:
        rule_set_name = re.search(r"[a-z]+", row_d).group()
        rule_string = row_d.replace(rule_set_name, "").replace("{", "").replace("}", "")
        rules_list = rule_string.split(",")
        for rule in rules_list:
            search = re.findall("([a-z]+)([<>])(\d+).(\w+)", rule)
            if search:
                name, op, val, dest = search[0]
                rule_function = eval(f"lambda part_dict: '{dest}' if part_dict['{name}'] {op} {val} else None")

                val = int(val)

                split_rules[rule_set_name].append((name, op, val, dest))
            else:
                rule_function = eval(f"lambda _: '{rule}'")
                split_rules[rule_set_name].append((rule,))

            rules[rule_set_name].append(rule_function)

    if not row_d:
        input_for_parts = True

tot = 0
for part in parts:
    queue = ['in']
    while queue:
        rule_set = queue.pop(0)
        for rule in rules[rule_set]:
            n_dest = rule(part)

            if n_dest == "R":
                break

            if n_dest == "A":
                tot += sum([val for val in part.values()])
                break

            if n_dest:
                queue.append(n_dest)
                break

print(f"Part1: {tot}, Check is {tot == 480738}")

parts_sets = [({'x': (1, 4001), 'm': (1, 4001), 'a': (1, 4001), 's': (1, 4001)}, 'in', 0)]

combi = 0
while parts_sets:
    part_set = parts_sets.pop(0)
    set_part, loc, i = part_set

    if loc == "A":
        combi += np.prod([x[1] - x[0] for x in set_part.values()])

    if loc in "AR":
        continue

    if len(split_rules[loc][i]) == 1:
        dest = split_rules[loc][i][0]
        parts_sets.append((set_part, dest, 0))
        continue

    name, op, val, dest = split_rules[loc][i]


    def split_rule(set_part_loc):
        _set_part, _loc, _i = set_part_loc
        set_1 = deepcopy(_set_part)
        set_2 = deepcopy(_set_part)
        lower, upper = _set_part[name]

        if op_map[op](lower, val) and op_map[op](upper, val):
            set_1[name] = (lower, upper)
            return [(set_1, dest, 0)]

        elif opp_op_map[op](lower, val) and opp_op_map[op](upper, val):
            set_1[name] = (lower, upper)
            return [(set_1, _loc, _i + 1)]

        elif op == "<":
            set_1[name] = (lower, val)
            set_2[name] = (val, upper)
            return [(set_1, dest, 0), (set_2, _loc, _i + 1)]

        elif op == ">":
            set_1[name] = (lower, val + 1)
            set_2[name] = (val + 1, upper)
            return [(set_1, _loc, _i + 1), (set_2, dest, 0)]


    parts_sets.extend(split_rule(part_set))

print(f"Part2: {combi}, Check is {combi == 131550418841958}")
