with open('day2_input') as f:
    lines = f.readlines()

score_mapping = dict(
    win=6,
    draw=3,
    lose=0,
    rock=1,
    paper=2,
    scissors=3
)

input_mapping = dict(
    A="rock",
    B="paper",
    C="scissors",
    X="rock",
    Y="paper",
    Z="scissors",
    x="lose",
    y="draw",
    z="win"
)

score_hierarchy = ["scissors", "rock", "paper"]


def check_game(op_play, my_play):
    my_index = score_hierarchy.index(my_play)
    op_index = score_hierarchy.index(op_play)

    if my_index == op_index:
        return "draw"
    if (my_index + 1) % 3 == op_index:
        return "lose"
    elif (my_index + 2) % 3 == op_index:
        return "win"


def what_to_play(op_play, result):
    op_index = score_hierarchy.index(op_play)
    if result == "win":
        my_index = (op_index + 1) % 3
    elif result == "lose":
        my_index = (op_index + 2) % 3
    elif result == "draw":
        my_index = op_index

    return score_hierarchy[my_index]


total_score = 0
for line in lines:
    my_play = input_mapping[line[2]]
    op_play = input_mapping[line[0]]
    total_score += score_mapping[my_play]

    result = check_game(op_play, my_play)
    total_score += score_mapping[result]
print(f"Part1: {total_score}")

total_score = 0
for line in lines:
    result = input_mapping[line[2].lower()]
    total_score += score_mapping[result]

    op_play = input_mapping[line[0]]
    my_play = what_to_play(op_play, result)
    total_score += score_mapping[my_play]

print(f"Part2: {total_score}")
