from math import floor

with open("day10_input") as f:
    data = f.read().splitlines()

error_score_mapping = {")": 3, "]": 57, "}": 1197, ">": 25137}
compl_score_mapping = {")": 1, "]": 2, "}": 3, ">": 4}
closing_bracket_pairing = {")": "(", "]": "[", "}": "{", ">": "<"}
opening_bracket_pairing = {val: key for key, val in closing_bracket_pairing.items()}

error_score = 0
compl_scores = []
chars = []
for syntax in data:
    queue = []
    for char in syntax:
        if char in "([{<":
            queue.append(char)

        elif closing_bracket_pairing[char] == queue[-1]:
            queue.pop(-1)

        else:
            chars.append(char)
            error_score += error_score_mapping[char]
            queue = []
            break

    if queue:
        compl_score = 0
        for char in reversed(queue):
            compl_score *= 5
            compl_score += compl_score_mapping[opening_bracket_pairing[char]]
        compl_scores.append(compl_score)

compl_scores_sorted = sorted(compl_scores)

print(f"Part1: {error_score}")
print(f"Part2: {compl_scores_sorted[floor(len(compl_scores) / 2)]}")
