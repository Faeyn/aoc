from collections import defaultdict
from functools import cache

with open('day22input') as f:
    data = f.read().splitlines()

def mix(mix_value, secret):
    return int(mix_value ^ secret)


def prune(secret):
    return secret % 16777216


def mix_and_prune(mix_value, secret):
    return prune(mix(mix_value, secret))

@cache
def get_next_secret(secret):
    secret = mix_and_prune(secret * 64, secret)
    secret = mix_and_prune(int(secret/32), secret)
    secret = mix_and_prune(secret * 2048, secret)
    return secret

ans = 0

val = defaultdict(lambda: 0)
for s in data:
    cp = int(str(s[-1]))
    sec = []
    seen = set()
    for _ in range(2000):
        s = get_next_secret(int(s))
        np = int(str(s)[-1])

        sec.append(np - cp)
        cp = np

        if len(sec) == 5:
            sec.pop(0)

        ct = tuple(sec)

        if ct in seen:
            continue

        seen.add(ct)
        val[ct] += np

    ans += s

print(ans)

max_banana = 0
sec = []
for k,v in val.items():
    max_banana = max(v, max_banana)
    if max_banana == v:
        sec = k

print(max_banana, sec)