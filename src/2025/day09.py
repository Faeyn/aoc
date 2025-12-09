from pathlib import Path
from itertools import product

with open(Path(__file__).parent / ".input/day09_input") as f:
    data = f.read()

# data = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3
# """

data = data.splitlines()

coords = [[int(nr) for nr in line.split(",")] for line in data]
coords_nr = len(coords)

def get_area(i, j):
    return (abs(coords[i][0] - coords[j][0]) + 1) * (abs(coords[i][1] - coords[j][1]) + 1)

max_area = float("-inf")
for i in range(coords_nr):
    for j in range(i + 1, coords_nr):
        max_area = max(max_area, get_area(i,j))
print(max_area)

def get_alignment(c1, c2):
    if c1[0] == c2[0]:
        return "ROW"
    if c1[1] == c2[1]:
        return "COL"

edges = [(coords[i], coords[(i+1)%coords_nr]) for i in range(coords_nr)]

def has_crossed(e1, e2):
    al1 = get_alignment(*e1)
    al2 = get_alignment(*e2)
    if al1 == al2:
        return False
    h_edge = e1 if al1 == "ROW" else e2
    v_edge = e1 if al1 == "COL" else e2

    h_edge_lower = min(h_edge[0][1], h_edge[1][1])
    h_edge_upper = max(h_edge[0][1], h_edge[1][1])
    
    v_edge_lower = min(v_edge[0][0], v_edge[1][0])
    v_edge_upper = max(v_edge[0][0], v_edge[1][0])
    if v_edge_lower <= h_edge[0][0] <=v_edge_upper and (h_edge_lower <= v_edge[0][1] and h_edge_upper >= v_edge[0][1]):
        return True

    return False

def get_valid_area(i, j):
    c1 = coords[i]
    c2 = coords[j]
    
    min_row = min(c1[0], c2[0]) + 1
    max_row = max(c1[0], c2[0]) - 1

    min_col = min(c1[1], c2[1]) + 1
    max_col = max(c1[1], c2[1]) - 1

    square_coords = [[min_row, min_col], [min_row, max_col], [max_row, max_col], [max_row, min_col]]
    square_edges = [(square_coords[k], square_coords[(k+1)%4]) for k in range(4)]

    hc = False
    for edge_s in square_edges:
        for edge in edges:
            hc = has_crossed(edge_s, edge)
            if hc:
                break
        if hc:
            break
    if hc:
        return False

    return get_area(i, j)


max_area = float("-inf")
for i in range(coords_nr):
    for j in range(i + 1, coords_nr):
        area = get_valid_area(i, j)
        if not area:
            continue
        max_area = max(max_area, area)

print(max_area)
                
