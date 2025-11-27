import re
from collections import defaultdict
from math import ceil

with open('day14_input') as f:
    data = f.read().splitlines()

start_string = data[0]

pattern = r"(\w+) -> (\w+)"

matches = {}
for row in data:
    if not re.search(pattern, row):
        continue
    key, val = re.findall(pattern, row)[0]
    matches[key] = key[0] + val, val + key[1]
pairs = {pair: len(re.findall(pair, start_string)) for pair in matches}


def get_score(_pairs):
    char_count = defaultdict(lambda: 0)
    for pair, occurrence in _pairs.items():
        for char in pair:
            char_count[char] += occurrence

    counts = [ceil(val / 2) for val in char_count.values()]
    return max(counts) - min(counts)


def update_pairs(_pairs):
    new_pairs = defaultdict(lambda: 0)
    for pair, occurrence in _pairs.items():
        for update_pair in matches[pair]:
            new_pairs[update_pair] += occurrence

    return new_pairs


for step in range(1, 41):
    pairs = update_pairs(pairs)

    if step == 10:
        print(f"Part1: {get_score(pairs)}")

print(f"Part2: {get_score(pairs)}")
