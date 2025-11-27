from collections import Counter
from time import time
from functools import cache
from math import floor

from advent_code.aoc_utils import get_nums

with open('day11_input') as f:
    data = f.read()

nrs = get_nums(data)

@cache
def stone_rules(nr, it):
    if it == 0:
        return 1

    if nr == 0:
        return stone_rules(1, it-1)
    elif len(str(nr)) % 2 == 0:
        l = floor(len(str(nr))/2)
        return stone_rules(int(str(nr)[:l]), it-1) + stone_rules(int(str(nr)[l:]), it-1)
    else:
        return stone_rules(nr * 2024, it-1)

ans = 0
for nr in nrs:
    ans += stone_rules(nr, 25)
print(ans)


start_time = time()
ans = 0
for nr in nrs:
    ans += stone_rules(nr, 75)
# print(ans)
print('mine', time() - start_time)

def main() -> None:
    with open('day11_input') as f:
        data = f.read().strip()

    stones = list(map(int, data.split()))
    counts = Counter(stones)

    for _ in range(75):
        new_counts = Counter()

        for stone, cnt in counts.items():
            if stone == 0:
                new_counts[1] += cnt
                continue

            num = str(stone)
            if len(num) % 2 == 0:
                new_counts[int(num[: len(num) // 2])] += cnt
                new_counts[int(num[len(num) // 2 :])] += cnt
            else:
                new_counts[stone * 2024] += cnt

        counts = new_counts

    # print(sum(counts.values()))


if __name__ == "__main__":
    start_time = time()
    main()
    print('jasper', time()-start_time)