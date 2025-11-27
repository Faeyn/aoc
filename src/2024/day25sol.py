with open('day25input') as f:
    data = f.read()

key_locks = data.split("\n\n")

keys, locks = [], []
for key_lock in key_locks:
    key_lock = key_lock.split("\n")

    key_lock_t = tuple(x.count("#") - 1 for x in list(map(list, zip(*key_lock))))
    if key_lock[0][0] == '#':
        locks.append(key_lock_t)
    else:
        keys.append(key_lock_t)

ans = 0
for key in keys:
    for lock in locks:
        if all([x + y <= 5 for x, y in zip(key, lock)]):
            ans += 1

print(ans)
