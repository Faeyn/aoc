from collections import defaultdict
from pprint import pprint

with open('day9_input') as f:
    data = f.read()

# data = "54321"

disk = []
file = 0
len_check = 0

file_blocks = []
free_blocks = []
for idx, num in enumerate(data):
    if idx % 2 == 0:
        file_blocks.append((int(num), str(file), len(disk)))
        disk.extend([str(file)] * int(num))
        file += 1
        len_check += int(num)

    else:
        free_blocks.append((len(disk), int(num)))
        disk.extend(['.'] * int(num))


disk2 = [x for x in disk]

idx = 0
to_stop = False
while idx < len(disk):
    if disk[idx] != '.':
        idx += 1
        continue

    last = '.'
    while last == '.' and idx < len(disk)-1:
        last = disk.pop()

    disk[idx] = last

    idx += 1

print(sum([i*int(v) for i, v in enumerate(disk) if v != '.']))

for f_block, file_idx, loc_idx in file_blocks[::-1]:
    for i_fb, (f_idx, size) in enumerate(free_blocks):
        if size >= f_block:
            if f_idx < loc_idx:
                free_blocks[i_fb] = (f_idx + f_block, size - f_block)
                disk2[f_idx:f_idx+f_block] = [file_idx]*f_block
                disk2[loc_idx: loc_idx+f_block] = ['.']*f_block
                break

print(sum([i*int(v) for i, v in enumerate(disk2) if v != '.']))
