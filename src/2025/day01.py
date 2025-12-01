import operator as o

f = open('.input/day01_input')
data = f.read()
f.close()
data = data.splitlines()

input = []
for line in data:
    input.append((line[0], int(line[1:])))

input_mapping = {'R': o.add, 'L': o.sub}
mapping = list(range(0, 100))

pos_c = 50
count = 0
count_2 = 0

for op in input:
    full_rotation, change = divmod(op[1], 100)
    pos_p = pos_c
    pos_c = input_mapping[op[0]](pos_c, change)

    if pos_c >= 100 or (pos_p > 0 and pos_c <= 0):
        count_2 += 1

    count_2 += full_rotation

    pos_c %= 100
    if pos_c == 0:
        count += 1

print('Part1: ', count)
print('Part2: ', count_2)

