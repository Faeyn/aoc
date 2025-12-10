from pathlib import Path
import numpy as np
from scipy.optimize import linprog

with open(Path(__file__).parent / ".input/day10") as f:
    data = f.read()

# data ="""[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
# """

data = data.splitlines()

ms1, ms2 = [], []
for i, line in enumerate(data):
    instruction = line.split(" ")
    end_state = instruction[0][1:-1]
    qnt = len(end_state)
    end_state = int(f'0b{"".join("1" if s == "#" else "0" for s in end_state)}', 2)

    buttons = [eval(x) for x in instruction[1:-1]]

    b1, b2 = [], []
    for button in buttons:
        b = ["0"] * qnt
        button = [button] if isinstance(button, int) else button
        for i in button:
            b[i] = "1"
        b2.append([int(x) for x in b])
        b1.append(int(f'0b{"".join(b)}', 2))

    joltage = [int(x) for x in instruction[-1][1:-1].split(",")]

    ms1.append((end_state, b1))
    ms2.append((joltage, b2))


def bfs(end_state, buttons):
    q = [(i, 0, 0, 0) for i in range(len(buttons))]

    global_state = set()
    while q:
        i_b, visited, state, pressed = q.pop(0)
        pressed += 1
        visited += 1 << i_b
        state ^= buttons[i_b]

        if state == end_state:
            return pressed
        
        if visited in global_state:
            continue
        global_state.add(visited)

        for idx in range(len(buttons)):
            if visited ^ 1 << idx:
                q.append((idx, visited, state, pressed))
    return None

def solve(joltage, buttons):
    A = np.array(list(zip(*buttons)))
    b = np.array(joltage)
    c = [1] * len(buttons) 
    res = linprog(c, A_eq = A, b_eq = b, bounds = (0, None), method = "highs", integrality =1)
    return int(res.fun)

print("Part1: ", sum(bfs(*x) for x in ms1))
print("Part2: ", sum(solve(*x) for x in ms2))

