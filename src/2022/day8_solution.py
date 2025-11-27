from itertools import product

with open("day8_input") as f:
    lines = f.read().splitlines()

grid = []

for line in lines:
    grid.append([int(height) for height in line])

covered_tree = 0
rgt_boundary = len(grid[0])
bot_boundary = len(grid)
x_boundary = [0, rgt_boundary - 1]
y_boundary = [0, bot_boundary - 1]

scenic_score = 0
for i_x, i_y in product(range(rgt_boundary), range(bot_boundary)):
    if i_x in x_boundary or i_y in y_boundary:
        covered_tree += 1
        continue

    row = grid[i_y]
    height = row[i_x]
    col = [row[i_x] for row in grid]

    if (
            height > max(row[:i_x]) or
            height > max(row[i_x + 1:]) or
            height > max(col[:i_y]) or
            height > max(col[i_y + 1:])):
        covered_tree += 1

        ss_lft = len(row[:i_x]) if max(row[:i_x]) < height else list(map(lambda i: i >= height, reversed(row[:i_x]))).index(True)+1
        ss_rgt = len(row[i_x+1:]) if max(row[i_x+1:]) < height else list(map(lambda i: i >= height, row[i_x+1:])).index(True)+1
        ss_top = len(col[:i_y]) if max(col[:i_y]) < height else list(map(lambda i: i >= height, reversed(col[:i_y]))).index(True)+1
        ss_bot = len(col[i_y+1:]) if max(col[i_y+1:]) < height else list(map(lambda i: i >= height, col[i_y+1:])).index(True)+1

        current_scenic_score = ss_lft * ss_rgt * ss_bot * ss_top

        scenic_score = scenic_score if scenic_score > current_scenic_score else current_scenic_score

print(f"Part1: {covered_tree}")
print(f"Part2: {scenic_score}")
