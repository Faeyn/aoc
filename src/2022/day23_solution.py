import pstats

import numpy as np

with open("day23_input") as f:
    lines = f.read().splitlines()


def main():
    def get_ans(elves, to_print=False):
        max_row, max_col, min_row, min_col = float("-inf"), float("-inf"), float("inf"), float("inf")
        for elf in elves:
            max_row = max(max_row, elf[0])
            min_row = min(min_row, elf[0])
            max_col = max(max_col, elf[1])
            min_col = min(min_col, elf[1])

        if to_print:
            for row in range(max_row + 1 - min_row):
                line = ""
                for col in range(max_col + 1 - min_col):
                    if (row + min_row, col + min_col) in elves:
                        line += "#"
                    else:
                        line += "."
                print(line)

        rectangle = (max_row - min_row + 1) * (max_col - min_col + 1)
        return rectangle - len(elves)

    elves = []

    for row, line in enumerate(lines):
        for col, cell in enumerate(line):
            if cell == "#":
                elves.append((row, col))

    elves_set = set(elves)

    move_order = ["N", "S", "W", "E"]
    move_checks = {
        "N": [(-1, 0), (-1, -1), (-1, 1)],
        "S": [(1, 0), (1, 1), (1, -1)],
        "W": [(0, -1), (1, -1), (-1, -1)],
        "E": [(0, 1), (1, 1), (-1, 1)]
    }

    def add_tuples(tup1, tup2):
        return tuple(x + y for x, y in zip(tup1, tup2))

    def find_proposal(elf):
        new_position = None
        has_neighbor = False
        for move in move_order:
            moves = move_checks[move]
            if not (add_tuples(elf, moves[0]) in elves_set or add_tuples(elf, moves[1]) in elves_set or add_tuples(elf,
                                                                                                                   moves[
                                                                                                                       2]) in elves_set):
                if new_position is None:
                    new_position = add_tuples(elf, move_checks[move][0])
            else:
                has_neighbor = True

        if has_neighbor and new_position:
            return new_position
        else:
            return elf

    for round in range(1000):
        print(round)
        elf_proposal = []
        for elf in elves:
            new_proposal = find_proposal(elf)

            if new_proposal in elf_proposal:
                index_conflict = elf_proposal.index(new_proposal)
                elf_proposal[index_conflict] = elves[index_conflict]

                elf_proposal.append(elf)

            else:
                elf_proposal.append(new_proposal)

        move_order.append(move_order.pop(0))

        if set(elves) == set(elf_proposal):
            print(f"Part2: {round + 1}")
            break

        elves = elf_proposal
        elves_set = set(elves)

        if round == 10 - 1:
            ans = get_ans(elves)
            print(f"Part1: {ans}")


main()

# import cProfile
#
# cProfile.run("main()", "profile_stats")
#
# stats = pstats.Stats('profile_stats')
# stats.sort_stats('cumulative')
# stats.print_stats()
