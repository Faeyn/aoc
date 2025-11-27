import re

with open("day4_input") as f:
    data = f.read().splitlines()

pattern = r"(\d+)"

games = []
for row in data:
    _, game_data = row.split(":")
    opened_numbers, check_numbers = game_data.split("|")
    opened_numbers, check_numbers = re.findall(pattern, opened_numbers), re.findall(pattern, check_numbers)
    winning_numbers = set(opened_numbers).intersection(set(check_numbers))
    score = 2 ** (len(winning_numbers) - 1) if len(winning_numbers) else 0

    games.append({"winning_nr": len(winning_numbers), "copies": 1, "score": score})

total_points = sum([data_point["score"] for data_point in games])

print(f"Part1: {total_points}")

stack_length = len(games)
for index, game_data_point in enumerate(games):
    for i in range(game_data_point["winning_nr"]):
        card_index = index + i + 1
        if card_index <= stack_length:
            games[card_index]["copies"] += game_data_point["copies"]

total_cards = sum([data_point["copies"] for data_point in games])

print(f"Part2: {total_cards}")
