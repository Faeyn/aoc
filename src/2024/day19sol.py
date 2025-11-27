from functools import cache
from advent_code.aoc_utils import get_words
import re

with open('day19input') as f:
    data = f.read().splitlines()

patterns = get_words(data[0])
target_patterns = data[2:]


@cache
def match(t_pattern):
    if len(t_pattern) == 0:
        return True

    for p in patterns:
        has_match = re.match(f'^{p}', t_pattern)
        if has_match:
            res = match(t_pattern[has_match.end():])
            if res:
                return True

    return False


print('Ans1: ', sum(match(pattern) for pattern in target_patterns))


@cache
def match_combos(t_pattern):
    if len(t_pattern) == 0:
        return 1

    combos = 0
    for p in patterns:
        has_match = re.match(f'^{p}', t_pattern)
        if has_match:
            combos += match_combos(t_pattern[has_match.end():])

    return combos


print('Ans2: ', sum(match_combos(pattern) for pattern in target_patterns))
