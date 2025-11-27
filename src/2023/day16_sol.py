from advent_code.coord import Coord

with open('day16_input') as f:
    data = f.read().splitlines()

dir_map = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}
symbol_mapping = {
    "\\": {"R": "D", "D": "R", "L": "U", "U": "L"},
    "/": {"R": "U", "U": "R", "L": "D", "D": "L"},
    "|": {"L": "UD", "R": "UD", "D": "D", "U": "U"},
    "-": {"L": "L", "R": "R", "D": "LR", "U": "LR"},
    ".": {"L": "L", "R": "R", "D": "D", "U": "U"}
}

width = len(data[0])
height = len(data)


def bfs_energized_tiles(start):
    queue = [start]
    visited = set()
    while queue:
        coord, direction = queue.pop(0)

        new_pos = coord + dir_map[direction]
        if (new_pos, direction) in visited:
            continue

        if 0 <= new_pos.row_i < height and 0 <= new_pos.col_i < width:
            visited.add((new_pos, direction))
            moves = symbol_mapping[data[new_pos.row_i][new_pos.col_i]][direction]
            queue.extend((new_pos, d) for d in moves)

    return len(set([item[0] for item in visited]))


if __name__ == "__main__":
    sol_1 = bfs_energized_tiles((Coord(0, -1), "R"))

    print(f"Part1: {sol_1}: Check {sol_1 == 6816}")
    max_energy = 0
    for i in range(width):
        max_energy = max(max_energy,
                         bfs_energized_tiles((Coord(-1, i), "D")),
                         bfs_energized_tiles((Coord(height, i), "U")),
                         bfs_energized_tiles((Coord(i, -1), "R")),
                         bfs_energized_tiles((Coord(i, width), "L"))
                         )

    print(f"Part2: {max_energy}: Check {max_energy == 8163}")
