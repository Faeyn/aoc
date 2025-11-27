import re
from collections import namedtuple
from day5_func import seed_to_location_ranges

with open("day5_input") as f:
    data = f.read().splitlines()

MapRange = namedtuple("MapRange", ["dest", "source", "range"])
seeds = [eval(x) for x in re.findall(r"(\d+)", data[0])]

seed_to_soil = [MapRange(*[eval(x) for x in re.findall(r"(\d+)", row)]) for row in data[3:34]]
soil_to_fertilizer = [MapRange(*[eval(x) for x in re.findall(r"(\d+)", row)]) for row in data[36:83]]
fertilizer_to_water = [MapRange(*[eval(x) for x in re.findall(r"(\d+)", row)]) for row in data[85:130]]
water_to_light = [MapRange(*[eval(x) for x in re.findall(r"(\d+)", row)]) for row in data[132:175]]
light_to_temperature = [MapRange(*[eval(x) for x in re.findall(r"(\d+)", row)]) for row in data[177:197]]
temperature_to_humidity = [MapRange(*[eval(x) for x in re.findall(r"(\d+)", row)]) for row in data[199:216]]
humidity_to_location = [MapRange(*[eval(x) for x in re.findall(r"(\d+)", row)]) for row in data[218:236]]

mappings = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature,
            temperature_to_humidity, humidity_to_location]

def get_min_location(seed_ranges):
    return min([val for pair in seed_to_location_ranges(seed_ranges, mappings) for val in pair])


seed_ranges = [(start, start + 1) for start in seeds]
print(f"Part1: {get_min_location(seed_ranges)}: 227653707")

seed_ranges = [(start, start + _range - 1) for start, _range in zip(seeds[::2], seeds[1::2])]
print(f"Part2: {get_min_location(seed_ranges)}: 78775051")
