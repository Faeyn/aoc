f = open('src/2025/.input/day03_input')
data = f.read()
f.close()

# data = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

data = data.splitlines()
    
def joltage(bank: str, batteries: int) -> int:
    out = []
    l = 0
    for r in reversed(range(batteries)):
        segment = bank[l:None if r == 0 else -r]
        _max = max(segment)
        l += segment.index(_max) + 1
        out.append(_max)

    return int("".join(out))

part_1, part_2 = 0, 0
for bank in data:
    part_1 += joltage(bank, 2)
    part_2 += joltage(bank, 12)

print("Part1: ", part_1)
print("Part2: ", part_2)