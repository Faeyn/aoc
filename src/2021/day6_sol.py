with open("day6_input") as f:
    data = f.read()

fishes_data = [eval(val) for val in data.split(",")]

new_fish_groups = {}
for day in range(9):
    new_fish_groups[day] = fishes_data.count(day)

for day in range(1, 257):
    old_fish_groups = {key: val for key, val in new_fish_groups.items()}
    new_fish_groups = {}
    for group_day in range(1, 9):
        new_fish_groups[group_day - 1] = old_fish_groups[group_day]

    new_fish_groups[6] += old_fish_groups[0]
    new_fish_groups[8] = old_fish_groups[0]

    if day == 80:
        fishes = sum([val for val in new_fish_groups.values()])
        print(f"Print1: {fishes}")

fishes = sum([val for val in new_fish_groups.values()])
print(f"Print2: {fishes}")
