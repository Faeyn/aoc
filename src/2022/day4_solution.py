from collections import namedtuple

SectionRanges = namedtuple("SectionRanges", ["lower", "upper"])


class Day4:
    def __init__(self, input_file):
        with open(input_file) as f:
            lines = f.read().splitlines()

        self.all_pairing = []

        for line in lines:
            section_ranges = line.split(",")

            lower_section_1 = eval(section_ranges[0].split("-")[0])
            upper_section_1 = eval(section_ranges[0].split("-")[1])

            lower_section_2 = eval(section_ranges[1].split("-")[0])
            upper_section_2 = eval(section_ranges[1].split("-")[1])

            self.all_pairing.append(
                (
                    SectionRanges(lower_section_1, upper_section_1),
                    SectionRanges(lower_section_2, upper_section_2)
                )
            )

    def get_fully_encased_sections(self):
        nr_overlap = 0
        for pair in self.all_pairing:
            overlap = False

            for i1, i2 in [(0, 1), (1, 0)]:
                range_1 = pair[i1]
                range_2 = pair[i2]

                if all(range_1.lower <= section <= range_1.upper for section in [range_2.lower, range_2.upper]):
                    overlap = True

            if overlap:
                nr_overlap += 1
        return nr_overlap

    def get_any_overlap_section(self):

        nr_overlap = 0
        for pair in self.all_pairing:
            overlap = False
            for i1, i2 in [(0, 1), (1, 0)]:
                range_1 = pair[i1]
                range_2 = pair[i2]

                if any(range_1.lower <= section <= range_1.upper for section in [range_2.lower, range_2.upper]):
                    overlap = True
                elif any(range_1.lower <= section <= range_1.upper for section in [range_2.lower, range_2.upper]):
                    overlap = True

            if overlap:
                nr_overlap += 1
        return nr_overlap


if __name__ == "__main__":
    sol = Day4("day4_input")
    print(f"Part1: {sol.get_fully_encased_sections()}")
    print(f"Part2: {sol.get_any_overlap_section()}")
