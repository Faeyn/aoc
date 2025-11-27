import functools
import itertools
import time
import cProfile
from collections import defaultdict, deque, namedtuple
from pprint import pprint

with open("day16_input") as f:
    lines = f.read().splitlines()


class ValveMap:
    opening_time = 1
    flow = {}
    connections = {}
    bit_mapping = []
    pressure_cache = {}
    pressure_cache_2 = {}

    def add_valve(self, valve: str, flow: int, connections: list[str]):
        if flow:
            self.bit_mapping.append(valve)
        self.flow[valve] = flow
        self.connections[valve] = connections

    @functools.cached_property
    def distance_mapping(self):
        """
        Distance map from a starting point
        """

        dist = defaultdict(lambda: defaultdict(lambda: float("inf")))
        for valve, flow in self.flow.items():
            if valve != "AA" and not flow:
                continue

            visited = {valve}
            queue = deque([(0, valve)])

            while queue:
                distance, position = queue.popleft()
                moved = distance + 1
                for next_valve in self.connections[position]:
                    if next_valve == valve:
                        continue

                    if next_valve not in visited:
                        visited.add(next_valve)
                        queue.append((moved, next_valve))

                    if self.flow[next_valve] and moved < dist[valve][next_valve]:
                        dist[valve][next_valve] = moved
        return dist

    @functools.cache
    def dfs(self, time, position, bitmask):
        max_pressure = 0

        for next_valve in self.distance_mapping[position]:
            valve_bit = 1 << self.bit_mapping.index(next_valve)
            if valve_bit & bitmask:
                continue

            time_after_actions = time - self.distance_mapping[position][next_valve] - self.opening_time

            if time_after_actions < 1:
                continue

            pressure_next_valve = time_after_actions * self.flow[next_valve]

            pressure = self.dfs(time_after_actions, next_valve, valve_bit | bitmask) + pressure_next_valve
            max_pressure = pressure if pressure > max_pressure else max_pressure

        return max_pressure


if __name__ == "__main__":
    valve_map = ValveMap()
    for line in lines:
        split_line = line.split(" ")
        name = split_line[1]
        flow = eval(split_line[4].replace("rate=", "").replace(";", ""))
        connections = [valve.replace(",", "") for valve in split_line[9:]]

        valve_map.add_valve(valve=name, flow=flow, connections=connections)

    all_open_valves_bit = (2 ** len(valve_map.bit_mapping) - 1)

    # cProfile.run("valve_map.dfs(30, 'AA', 0)", sort="cumulative")

    start_time_overal = time.time()
    m = 0
    for i in range(all_open_valves_bit):
        start_time = time.time()

        m = max(m, valve_map.dfs(26, "AA", i) + valve_map.dfs(26, "AA", all_open_valves_bit ^ i))

        print(i, bin(i), bin(all_open_valves_bit ^ i), time.time() - start_time)

    print(m, time.time() - start_time_overal)
