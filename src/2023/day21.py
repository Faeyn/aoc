from advent_code.coord import Coord

with open('day21_input') as f:
    data = f.read().splitlines()

length = len(data)

for row_i, r_data in enumerate(data):
    for col_i, cell in enumerate(r_data):
        if cell == "S":
            start = Coord(row_i, col_i)


def get_centers(r):
    sn = r * (r + 1)
    sn2 = (r - 1) * ((r - 1) + 1)
    if r % 2 == 1:
        return sn2 + r, sn + r + 1

    return sn + r + 1, sn2 + r


def get_corners(r):
    return 2 * r * (r + 1)


def get_nr_end_nodes(start, steps_limit):
    queue = [(start, 0)]
    visited = set()
    even = set()
    odd = set()
    while queue:
        c_node, steps = queue.pop(0)
        visited.add(c_node)

        if steps % 2 == 0:
            even.add(c_node)
        else:
            odd.add(c_node)

        if steps >= steps_limit:
            continue

        for n_node in c_node.get_adjacent():
            if n_node in visited or n_node in [t[0] for t in queue]:
                continue

            if not (0 <= n_node.row < length and 0 <= n_node.col < length):
                continue

            if data[n_node.row][n_node.col] == "#":
                continue

            queue.append((n_node, steps + 1))
    return len(odd), len(even)


_, part1 = get_nr_end_nodes(start, 64)

print(f"Part1: {part1}: Check is {part1 == 3768}")

m_odd, m_even = get_nr_end_nodes(start, 65)
ff_odd, ff_even = get_nr_end_nodes(start, 131)
c_odd_even = (ff_odd + ff_even) - (m_odd + m_even)

steps = 26501365  # input
rings, remainder = divmod(steps, length)

corners = get_corners(rings)
odd_centers, even_centers = get_centers(rings)

ans = int(corners / 2 * c_odd_even + odd_centers * m_odd + even_centers * m_even)
print(f"Part2: {ans}: Check is {ans == 627960775905777}")
