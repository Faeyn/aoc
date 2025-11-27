import re
from abc import ABC, abstractmethod
from copy import deepcopy
from enum import Enum

from icecream import ic

with open('day20_input') as f:
    data = f.read().splitlines()


class Pulse(Enum):
    high = "high"
    low = "low"


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


def get_system_state(pulsers):
    system_state = ""
    for pulser_name in sorted(pulsers):
        system_state += pulsers[pulser_name].state_repr()
    return system_state


if __name__ == "__main__":
    pulsers = {}

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

    nulls = set()
    for pulser, pulse_processor in pulsers.items():
        for dest_proc in pulse_processor.destinations:

            if dest_proc in pulsers:

                if isinstance(pulsers[dest_proc], Conjunction):
                    pulsers[dest_proc].add_origin(pulser)

            else:
                nulls.add(dest_proc)

    for nully in list(nulls):
        pulsers[nully] = NullProcessor([""], nully)

    pulse_counter = {Pulse.low: 0, Pulse.high: 0}
    states = {}
    states[get_system_state(pulsers)] = (0, deepcopy(pulse_counter))

    for cycle in range(1, 1001):
        queue = [('button', Pulse.low, 'broadcaster')]
        while queue:
            from_pulser, type_pulse, to_pulser = queue.pop(0)
            pulse_counter[type_pulse] += 1
            next_commands = pulsers[to_pulser].process_pulse(from_pulser, type_pulse)
            queue.extend(next_commands)

    print(f"Part1: {pulse_counter[Pulse.high] * pulse_counter[Pulse.low]}")
