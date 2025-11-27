with open('day2_input') as f:
    data = f.read().splitlines()


def is_safe(diffs):
    return (all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)) and all(abs(diff) < 4 for diff in diffs)


def get_diff(ls):
    return [int(ls[i + 1]) - int(ls[i]) for i in range(len(ls) - 1)]


ans1, ans2 = 0, 0
for row in data:
    items = row.split(' ')
    if is_safe(get_diff(items)):
        ans1 += 1
        ans2 += 1
        continue

    for idx in range(len(items)):
        if is_safe(get_diff(items[:idx] + items[idx+1:])):
            ans2 += 1
            break

print('ans1: ', ans1, 'ans2: ', ans2)