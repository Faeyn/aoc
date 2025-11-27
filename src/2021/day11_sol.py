from advent_code.coord import Coord

with open("day11_input") as f:
    data = f.read().splitlines()

octos = {}
for row, row_data in enumerate(data):
    for col, cell in enumerate(row_data):
        octos[Coord(row, col)] = eval(cell)


def print_octos(_octos):
    field = [[_octos[Coord(j, i)] for i in range(len(data[0]))] for j in range(len(data))]
    # pprint(field)


flashes = 0
print_octos(octos)
for step in range(1, 1000):
    for octo, energy in octos.items():
        octos[octo] += 1

    queue = [octo for octo in octos if octos[octo] > 9]
    flashed = set([octo for octo in queue])
    print_octos(octos)
    while queue:
        octo = queue.pop()
        conditions = [
            lambda coord: coord in octos
        ]

        for n_octo in octo.get_valid_surrounding(conditions=conditions):
            octos[n_octo] += 1
            if octos[n_octo] > 9 and n_octo not in flashed:
                flashed.add(n_octo)
                queue.append(n_octo)
        print_octos(octos)

    flashes += len([energy for energy in octos.values() if energy > 9])
    octos = {octo: energy if energy <= 9 else 0 for octo, energy in octos.items()}
    print_octos(octos)
    if step == 100:
        print(f"Part1: {flashes}")

    if all(energy == 0 for energy in octos.values()):
        print(f"Part2: {step}")
        break
