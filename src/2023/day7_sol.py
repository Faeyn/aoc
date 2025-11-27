import re
from functools import partial
from pprint import pprint

with open("day7_input") as f:
    data = f.read().splitlines()

card_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
card_order_joker = ["J"] + card_order[:9] + card_order[10:]

hands = [tuple(re.findall(r"(\w+)", row)) for row in data]

type_score = {(1, 1, 1, 1, 1): 1, (1, 1, 1, 2): 2, (1, 2, 2): 3, (1, 1, 3): 4, (2, 3): 5, (1, 4): 6, (5,): 7}
joker_mod = {
    (1, 1, 1, 1, 1): {0: 0, 1: 1}, (1, 1, 1, 2): {0: 0, 1: 2, 2: 2}, (1, 2, 2): {0: 0, 1: 2, 2: 3},
    (1, 1, 3): {0: 0, 1: 2, 3: 2}, (2, 3): {0: 0, 2: 2, 3: 2}, (1, 4): {0: 0, 1: 1, 4: 1}, (5,): {0: 0, 5: 0}
}


def get_type_score(hand, with_joker=False):
    hand_count = tuple(sorted([hand.count(card) for card in list(set(hand))]))
    return type_score[hand_count] + with_joker * joker_mod[hand_count][hand.count("J")]


def get_hand_score(hand_bid, func_det_type, order):
    hand, bid = hand_bid
    return func_det_type(hand) * 13 ** 5 + sum((order.index(hand[x]) + 1) * 13 ** (4 - x) for x in range(len(hand)))


def get_total_score(hands, func_det_type, order):
    sorted_hands = sorted(hands, key=partial(get_hand_score, func_det_type=func_det_type, order=order))
    return sum([index * eval(bid) for index, (_, bid) in enumerate(sorted_hands, start=1)])


score = get_total_score(hands, get_type_score, card_order)
print(f"Part1: {score}: {score == 251216224}")

score_jokers = get_total_score(hands, partial(get_type_score, with_joker=True), card_order_joker)
print(f"Part2: {score_jokers}: {score_jokers == 250825971}")
