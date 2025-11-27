a = [1,2,3,4,5]

for i, item in enumerate(a):
    for item2 in a[i+1:]:
        print(item, item2)