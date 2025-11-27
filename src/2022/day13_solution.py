from itertools import zip_longest

with open("day13_input") as f:
    lines = f.read().splitlines()

input_values = []
input_set = []

input_values_full = []
for line in lines:
    if line:
        input_ = eval(line)
        input_set.append(input_)
        input_values_full.append(input_)
    else:
        input_values.append(input_set)
        input_set = []


def compare_input(input_1, input_2):
    if isinstance(input_1, (int, float)) and isinstance(input_2, (int, float)):
        if input_1 < input_2:
            return True
        elif input_1 == input_2:
            pass
        else:
            return False
    else:
        if isinstance(input_1, list) and input_2 == float("-inf"):
            return False
        elif input_1 == float("-inf") and isinstance(input_2, list):
            return True

        input_1 = input_1 if isinstance(input_1, list) else [input_1]
        input_2 = input_2 if isinstance(input_2, list) else [input_2]

        for i_1, i_2 in zip_longest(input_1, input_2, fillvalue=float("-inf")):
            check = compare_input(i_1, i_2)
            if isinstance(check, bool):
                return check


total_score = 0
for index, input_set in enumerate(input_values, start=1):
    if compare_input(*input_set):
        total_score += index

print(f"Part1: {total_score}")

package_1 = [[2]]
package_2 = [[6]]

input_values_full.extend([package_1, package_2])


def bubbleSort(input_list):
    output_list = [x for x in input_list]
    n = len(output_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if compare_input(output_list[j + 1], output_list[j]):
                output_list[j], output_list[j + 1] = output_list[j + 1], output_list[j]
    return output_list


sorted_packages = bubbleSort(input_values_full)

print(f"Part2: {(sorted_packages.index(package_1) + 1) * (sorted_packages.index(package_2) + 1)}")
