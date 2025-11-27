import re
from abc import ABC, abstractmethod
from copy import deepcopy
from enum import Enum
import numpy as np
from icecream import ic
from sympy.ntheory.modular import solve_congruence

with open('day20_input') as f:
    data = f.read().splitlines()


class Pulse(Enum):
    high = "high"
    low = "low"
    null = 'null'


class PulseProcessor(ABC):
    def __init__(self, destinations, name):
        self.name = name
        self.destinations = deepcopy(destinations)

    @abstractmethod
    def process_pulse(self, origin, pulse: Pulse) -> list:
        pass

    def state_repr(self) -> str:
        return ""


class Button(PulseProcessor):
    def process_pulse(self, origin, pulse: Pulse):
        return [(self.name, pulse, destination) for destination in self.destinations]


class BroadCaster(PulseProcessor):
    def process_pulse(self, origin, pulse: Pulse):
        return [(self.name, pulse, destination) for destination in self.destinations]


class NullProcessor(PulseProcessor):
    def process_pulse(self, origin, pulse: Pulse):
        return []


class FlipFlop(PulseProcessor):
    def __init__(self, destinations, name):
        super().__init__(destinations, name)
        self.state = False

    def state_repr(self):
        return str(int(self.state))

    def process_pulse(self, origin, pulse: Pulse):
        if pulse == Pulse.high:
            return []

        self.state = not self.state
        if self.state:
            new_pulse = Pulse.high
        else:
            new_pulse = Pulse.low

        return [(self.name, new_pulse, destination) for destination in self.destinations]


class Conjunction(PulseProcessor):
    def __init__(self, destinations, name):
        super().__init__(destinations, name)
        self.state = {}
        self.origins = []

    def add_origin(self, origin):
        self.origins.append(origin)
        self.state[origin] = Pulse.low

    def process_pulse(self, origin, pulse: Pulse):
        self.state[origin] = pulse

        if all([val == Pulse.high for val in self.state.values()]):
            new_pulse = Pulse.low
        else:
            new_pulse = Pulse.high

        return [(self.name, new_pulse, destination) for destination in self.destinations]

    def state_repr(self):
        state = ""
        for origin in self.origins:
            state += "1" if self.state[origin] == Pulse.high else "0"
        return state


def get_system_state(pulsers, cluster=None):
    system_state = ""

    if cluster:
        names = sorted(cluster)
    else:
        names = sorted(pulsers)

    for pulser_name in names:
        system_state += pulsers[pulser_name].state_repr()
    return system_state


if __name__ == "__main__":
    pulsers = {}

    # Create all the pulse processors
    for row_data in sorted(data, key=lambda string: string[0]):
        pulser, to_pulser = row_data.split(" -> ")
        pulser_type = pulser[0]
        to_pulser = to_pulser.split(", ")

        if pulser_type == "%":
            pulsers[pulser[1:]] = FlipFlop(to_pulser, pulser[1:])

        elif pulser_type == "&":
            pulsers[pulser[1:]] = Conjunction(to_pulser, pulser[1:])

        else:
            pulsers[pulser] = BroadCaster(to_pulser, pulser)

        pulsers["button"] = Button(["broadcaster"], "button")

    # Populate the destinations of all the processors and catch undefined destinations
    nulls = set()
    for pulser, pulse_processor in pulsers.items():
        for dest_proc in pulse_processor.destinations:

            if dest_proc in pulsers:

                if isinstance(pulsers[dest_proc], Conjunction):
                    pulsers[dest_proc].add_origin(pulser)

            else:
                nulls.add(dest_proc)

    # Create Process pulsers that does not further process the pulse
    for nully in list(nulls):
        pulsers[nully] = NullProcessor([""], nully)

    clusters = [
        ["bx", "sp", "xc", "ff", "rv", "nx", "rn", "fn", "fk", "mv", "kn", "fx", "sk", "hr"],
        ["jq", "sv", "jt", "qt", "lj", "vk", "nk", "xk", "jm", "lp", "vp", "fb", "zb", "dt"],
        ["jp", "pg", "kt", "mb", "jc", "ph", "dx", "ct", "kd", "pp", "pz", "hp", "tx", "vr"],
        ["nv", "qs", "bc", "xb", "jf", "xm", "gv", "mh", "th", "hx", "nr", "jh", "vh", "cj"],
    ]

    sub_pulses = []
    for cluster in clusters:
        pulse_counter = {Pulse.low: 0, Pulse.high: 0}
        states = {}
        for cycle in range(1, 1_000_001):
            state = get_system_state(pulsers, cluster)

            if state in states:
                break

            states[state] = cycle, deepcopy(pulse_counter)

            queue = [('broadcaster', Pulse.low, cluster[0])]
            while queue:
                from_pulser, type_pulse, to_pulser = queue.pop(0)
                if from_pulser == cluster[1] and type_pulse == Pulse.high:
                    sub_pulses.append(cycle)

                pulse_counter[type_pulse] += 1
                next_commands = pulsers[to_pulser].process_pulse(from_pulser, type_pulse)
                queue.extend(next_commands)

part2 = np.lcm.reduce(sub_pulses)
print(f"Part2: {part2}, Check is {part2 == 233283622908263}")
