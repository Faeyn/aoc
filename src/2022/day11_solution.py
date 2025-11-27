from math import floor

monkey_info = {
    "0": dict(
        inventory=[73, 77],
        operation=lambda x: x * 5,
        test=lambda x: 0 if x % 11 == 0 else 1,
        throw=("6", "5"),
        inspect=0),
    "1": dict(
        inventory=[57, 88, 80],
        operation=lambda x: x + 5,
        test=lambda x: 0 if x % 19 == 0 else 1,
        throw=("6", "0"),
        inspect=0),
    "2": dict(
        inventory=[61, 81, 84, 69, 77, 88],
        operation=lambda x: x * 19,
        test=lambda x: 0 if x % 5 == 0 else 1,
        throw=("3", "1"),
        inspect=0),
    "3": dict(
        inventory=[78, 89, 71, 60, 81, 84, 87, 75],
        operation=lambda x: x + 7,
        test=lambda x: 0 if x % 3 == 0 else 1,
        throw=("1", "0"),
        inspect=0),
    "4": dict(
        inventory=[60, 76, 90, 63, 86, 87, 89],
        operation=lambda x: x + 2,
        test=lambda x: 0 if x % 13 == 0 else 1,
        throw=("2", "7"),
        inspect=0),
    "5": dict(
        inventory=[88],
        operation=lambda x: x + 1,
        test=lambda x: 0 if x % 17 == 0 else 1,
        throw=("4", "7"),
        inspect=0),
    "6": dict(
        inventory=[84, 98, 78, 85],
        operation=lambda x: x * x,
        test=lambda x: 0 if x % 7 == 0 else 1,
        throw=("5", "4"),
        inspect=0),
    "7": dict(
        inventory=[98, 89, 78, 73, 71],
        operation=lambda x: x + 4,
        test=lambda x: 0 if x % 2 == 0 else 1,
        throw=("3", "2"),
        inspect=0),
}

rounds = 20  # part 1
rounds = 10000  # part 2
for _ in range(rounds):
    for monkey in range(len(monkey_info)):
        rules = monkey_info[str(monkey)]
        inv = rules["inventory"]

        for _2 in range(len(rules["inventory"])):
            item_worry = rules["inventory"].pop(0)
            # item_worry = int(floor(rules["operation"](item_worry) / 3))  # part 1
            item_worry = int(floor(rules["operation"](item_worry))) % 9699690  # part 2 test_dir devisions multiplied
            monkey_info[rules["throw"][rules["test_dir"](item_worry)]]["inventory"].append(item_worry)
            rules["inspect"] += 1

sorted_monkey_business = sorted([x["inspect"] for x in monkey_info.values()])
ans = sorted_monkey_business[-1] * sorted_monkey_business[-2]
print(sorted_monkey_business)
print(ans)
