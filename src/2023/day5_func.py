def find_mapping_range(source_ranges, mapping):
    dest_ranges = set()
    chck_ranges = [_ for _ in source_ranges]

    while chck_ranges:
        min, max = chck_ranges.pop(0)

        in_range = False
        for map_range in mapping:
            des, src, rng = map_range.dest, map_range.source, map_range.range
            min_in_range = src <= min < src + rng
            max_in_range = src < max <= src + rng
            mod = des - src

            in_range = min_in_range or max_in_range or in_range

            if min_in_range:
                if max_in_range:
                    dest_ranges.add((min + mod, max + mod))
                else:
                    dest_ranges.add((min + mod, des + rng))
                    chck_ranges.append((src + rng, max))
            else:
                if max_in_range:
                    dest_ranges.add((des, max + mod))
                    chck_ranges.append((min, src))

                else:
                    dest_ranges.add((min, max))

        if in_range and (min, max) in dest_ranges:
            dest_ranges.remove((min, max))

    return list(dest_ranges)


def seed_to_location_ranges(seed_ranges, mappings):
    current_ranges = [_ for _ in seed_ranges]
    for mapping in mappings:
        current_ranges = find_mapping_range(current_ranges, mapping)
    return current_ranges
