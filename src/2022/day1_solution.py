import logging

with open('day1_input') as f:
    lines = f.readlines()

all_cal = []
cur_cal = 0
for line in lines:
    if line != "\n":
        cur_cal += float(line)
    else:
        all_cal.append(cur_cal)
        cur_cal = 0

print(f"Part1: {max(all_cal)}")

print(f"Part2: {sum(sorted(all_cal, reverse=True)[:3])}")
