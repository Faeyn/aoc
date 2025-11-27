from collections import namedtuple
from functools import cache, lru_cache
from time import time
import cProfile

import re
from collections import namedtuple
from typing import List

with open("day19_input") as f:
    lines = f.read()

pattern = r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian"
matches = re.findall(pattern, lines)

RobotMats = namedtuple('RobotMats', ["ore", "clay", "obsidian"])
BluePrint = namedtuple("BluePrint", ["number", "ore_bot", "clay_bot", "obsidian_bot", "geode_bot"])

blueprints: List[BluePrint] = []
for match in matches:
    blueprints.append(
        BluePrint(match[0],
                  RobotMats(eval(match[1]), 0, 0),
                  RobotMats(eval(match[2]), 0, 0),
                  RobotMats(eval(match[3]), eval(match[4]), 0),
                  RobotMats(eval(match[5]), 0, eval(match[6])),
                  )
    )

total_time = 24

State = namedtuple("State", ["ore", "clay", "obsidian", "geode", "ore_bot", "clay_bot", "obsidian_bot", "geode_bot"])
start_state = State(0, 0, 0, 0, 1, 0, 0, 0)


@cache
def dfs(time: int, state: State, blueprint: BluePrint):
    geode_geode_branch, geode_obsidian_branch, geode_clay_branch, geode_ore_branch, geode_continue = 0, 0, 0, 0, 0

    continue_branch = True

    ore_branch = state.ore >= blueprint.ore_bot.ore
    if state.ore_bot == max(
            [blueprint.ore_bot.ore, blueprint.clay_bot.ore, blueprint.geode_bot.ore, blueprint.obsidian_bot.ore]):
        ore_branch = False

    clay_branch = state.ore >= blueprint.clay_bot.ore
    if state.clay_bot == blueprint.obsidian_bot.clay:
        clay_branch = False

    obsidian_branch = state.ore >= blueprint.obsidian_bot.ore and state.clay >= blueprint.obsidian_bot.clay
    if state.obsidian_bot == blueprint.geode_bot.obsidian:
        obsidian_branch = False

    geode_branch = state.ore >= blueprint.geode_bot.ore and state.obsidian >= blueprint.geode_bot.obsidian

    if geode_branch:
        ore_branch, clay_branch, obsidian_branch, continue_branch = False, False, False, False

    if time == 2:
        ore_branch, clay_branch, obsidian_branch = False, False, False

    max_geode = state.geode

    if time == 0:
        return max_geode

    if continue_branch:
        geode_continue = dfs(time - 1, State(
            ore=state.ore + state.ore_bot,
            clay=state.clay + state.clay_bot,
            obsidian=state.obsidian + state.obsidian_bot,
            geode=state.geode + state.geode_bot,
            ore_bot=state.ore_bot,
            clay_bot=state.clay_bot,
            obsidian_bot=state.obsidian_bot,
            geode_bot=state.geode_bot
        ), blueprint)

    if ore_branch:
        geode_ore_branch = dfs(time - 1, State(
            ore=state.ore + state.ore_bot - blueprint.ore_bot.ore,
            clay=state.clay + state.clay_bot,
            obsidian=state.obsidian + state.obsidian_bot,
            geode=state.geode + state.geode_bot,
            ore_bot=state.ore_bot + 1,
            clay_bot=state.clay_bot,
            obsidian_bot=state.obsidian_bot,
            geode_bot=state.geode_bot
        ), blueprint)

    if clay_branch:
        geode_clay_branch = dfs(time - 1, State(
            ore=state.ore + state.ore_bot - blueprint.clay_bot.ore,
            clay=state.clay + state.clay_bot,
            obsidian=state.obsidian + state.obsidian_bot,
            geode=state.geode + state.geode_bot,
            ore_bot=state.ore_bot,
            clay_bot=state.clay_bot + 1,
            obsidian_bot=state.obsidian_bot,
            geode_bot=state.geode_bot
        ), blueprint)

    if obsidian_branch:
        geode_obsidian_branch = dfs(time - 1, State(
            ore=state.ore + state.ore_bot - blueprint.obsidian_bot.ore,
            clay=state.clay + state.clay_bot - blueprint.obsidian_bot.clay,
            obsidian=state.obsidian + state.obsidian_bot,
            geode=state.geode + state.geode_bot,
            ore_bot=state.ore_bot,
            clay_bot=state.clay_bot,
            obsidian_bot=state.obsidian_bot + 1,
            geode_bot=state.geode_bot
        ), blueprint)

    if geode_branch:
        geode_geode_branch = dfs(time - 1, State(
            ore=state.ore + state.ore_bot - blueprint.geode_bot.ore,
            clay=state.clay + state.clay_bot,
            obsidian=state.obsidian + state.obsidian_bot - blueprint.geode_bot.obsidian,
            geode=state.geode + state.geode_bot,
            ore_bot=state.ore_bot,
            clay_bot=state.clay_bot,
            obsidian_bot=state.obsidian_bot,
            geode_bot=state.geode_bot + 1
        ), blueprint)

    max_geode = max(max_geode, geode_geode_branch, geode_obsidian_branch, geode_clay_branch, geode_ore_branch,
                    geode_continue)
    return max_geode


if __name__ == "__main__":
    ans = 0
    for blueprint in blueprints:
        start_time = time()
        geode = dfs(24, start_state, blueprint)
        ans += geode * eval(blueprint.number)
        # print(blueprint.number, f"geodes: {geode}")
        # print(time() - start_time)

    print(f"Part1: {ans}")

    ans_2 = 1
    for blueprint in blueprints[:3]:
        start_time = time()
        geode = dfs(32, start_state, blueprint)
        ans_2 *= geode
        # print(blueprint.number, f"geodes: {geode}")
        # print(time() - start_time)

    print(f"Part2: {ans_2}")
