with open("day1_input") as f:
    data = f.read().splitlines()

list1, list2 = [], []
for x in data:
    e1, e2 = x.split("   ")
    list1.append(int(e1))
    list2.append(int(e2))

ans, ans2 = 0, 0
for x, y in zip(sorted(list1), sorted(list2)):
    ans += abs(x-y)
    ans2 += x * list2.count(x)

print(ans, ans2)
