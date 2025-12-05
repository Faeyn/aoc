from pathlib import Path
from datetime import datetime

f = open(Path(__file__).parent / '.input/day05_input')
data = f.read()
f.close()

# data = """3-5
# 10-14
# 16-20
# 12-18
#
# 1
# 5
# 8
# 11
# 17
# 32"""

fresh, ids = data.split("\n\n")
fresh = [(int(l), int(r)) for l, r in [f.split("-") for f in fresh.splitlines()]]
ids = [int(id) for id in ids.splitlines()]

start = datetime.now()

stack = [r for r in fresh]

f = []
while stack: 
    l, r = stack.pop()

    for i, (l2, r2) in enumerate(f):
        if r2 >= l and l2 <= r:
            f.pop(i)
            stack.append((min(l, l2), max(r, r2)))
            break
    else:
        f.append((l, r))


part_2 = sum([r+1 - l for l, r in f])
part_1 = sum([any([l <= id <= r for l, r in f]) for id in ids])

print("Part1: ", part_1)
print("Part2: ", part_2)

print(datetime.now() - start)
