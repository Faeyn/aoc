with open('day15input') as f:
    data = f.read().splitlines()

map = [list(row) for row in data[:50]]
moves = ''.join(data[51:])
h = len(map)
w = len(map[0])

move_mapping = {'>': (0, 1), '^': (-1, 0), '<': (0, -1), 'v': (1, 0)}

for row_i, row in enumerate(map):
    for col_i, cell in enumerate(row):
        if cell == '@':
            bot_location = (row_i, col_i)


def check_next_box(r, c, dr, dc):
    nr = r + dr
    nc = c + dc

    if map[nr][nc] == '#':
        return [], False

    if map[nr][nc] == '.':
        return [], True

    nodes, cont = check_next_box(nr, nc, dr, dc)

    if cont:
        return [(nr, nc)] + nodes, cont
    else:
        return [], cont


for move in moves:
    cr, cc = bot_location
    dr, dc = move_mapping[move]

    coords, to_move = check_next_box(cr, cc, dr, dc)

    if to_move:
        for xr, xc in reversed([(cr, cc)] + coords):
            map[xr + dr][xc + dc] = map[xr][xc]
        map[cr][cc] = '.'
        bot_location = cr + dr, cc + dc

ans = 0
for row_i, row in enumerate(map):
    for col_i, cell in enumerate(row):
        if cell == 'O':
            ans += 100 * row_i + col_i
print(ans)

new_map = []

for x in data[:50]:
    new_map.append(x.replace('#', '##').replace('.', '..').replace('@', '@.').replace('O', '[]'))

map = [list(row) for row in new_map]


for row_i, row in enumerate(map):
    for col_i, cell in enumerate(row):
        if cell == '@':
            bot_location = (row_i, col_i)

def check_box_up_down(r, c, dr, dc):
    nr = r + dr
    nc = c + dc

    if map[nr][nc] == '#':
        return [], False

    if map[nr][nc] == '.':
        return [], True

    c_box = []
    if map[nr][nc] == '[':
        c_box.append((nr, nc))
        c_box.append((nr, nc+1))
        nodes1, cont1 = check_box_up_down(nr, nc, dr, dc)
        nodes2, cont2 = check_box_up_down(nr, nc+1, dr, dc)
        node = list(set(nodes1 + nodes2))

    if map[nr][nc] == ']':
        c_box.append((nr, nc))
        c_box.append((nr, nc-1))
        nodes1, cont1 = check_box_up_down(nr, nc, dr, dc)
        nodes2, cont2 = check_box_up_down(nr, nc-1, dr, dc)
        node = list(set(nodes1 + nodes2))

    cont = cont1 & cont2
    if cont:
        return c_box + node, cont
    else:
        return [], cont

for move in moves:
    cr, cc = bot_location
    dr, dc = move_mapping[move]

    if move in '^v':
        coords, to_move = check_box_up_down(cr, cc, dr, dc)
        if to_move:
            for xr, xc in sorted([(cr, cc)] + coords, key=lambda x: x[0], reverse=dr == 1):
                map[xr + dr][xc + dc], map[xr][xc] = map[xr][xc], map[xr + dr][xc + dc]

            bot_location = cr + dr, cc + dc
    else:
        coords, to_move = check_next_box(cr, cc, dr, dc)
        if to_move:
            for xr, xc in sorted([(cr, cc)] + coords, key=lambda x: x[1], reverse=dc == 1):
                map[xr + dr][xc + dc], map[xr][xc] = map[xr][xc], map[xr + dr][xc + dc]
            bot_location = cr + dr, cc + dc

ans = 0
for row_i, row in enumerate(map):
    for col_i, cell in enumerate(row):
        if cell == '[':
            ans += 100 * row_i + col_i

print(ans)