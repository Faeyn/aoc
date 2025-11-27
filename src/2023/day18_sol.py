from icecream import ic

ic.disable()

part = 1
file = 'day18_input'
with open(file) as f:
    data = f.read().splitlines()


class Member:
    def __init__(self, row, cover, base):
        self.row = row
        self.cover = cover
        self.base = base

    @property
    def base_length(self):
        return self.base(1) - self.base(0)

    @property
    def cover_length(self):
        return self.cover(1) - self.cover(0)

    def __repr__(self):
        return f"Row: {self.row}, Cover: {self.cover}, Base: {self.base}"

    def __hash__(self):
        return self.row, self.cover, self.base


def parse_hex(hex_input):
    hex_map = {"0": "R", "1": "D", "2": "L", "3": "U"}
    return str(hex_map[hex_input[-2]]), str(int(hex_input[2:-2], 16))


mod_map = {"R": +1, "L": -1, "D": +1, "U": -1, }
opposite_dir = {"D": "U", "U": "D"}

dig_plan_1, dig_plan_2 = [], []
for row_data in data:
    dig_plan_1.append(row_data.split(" "))
    dig_plan_2.append(list(parse_hex(row_data.split(" ")[-1])))

dig_plans = [dig_plan_1, dig_plan_2]

for plan_i, dig_plan in enumerate(dig_plans):
    area = 0
    for op in dig_plan:
        dist = eval(op[1])

        area += dist


    def get_horizontal_members():
        row_i, col_i = 0, 0
        horizontal_members = []
        for index, op_in_plan in enumerate(dig_plan):
            prev_dir = dig_plan[index - 1][0]
            next_dir = dig_plan[(index + 1) % len(dig_plan)][0]
            direction, distance = op_in_plan[:2]
            distance = int(distance)

            if direction in "LR":
                val1 = col_i
                col_i += mod_map[direction] * distance
                val2 = col_i

                val_l, val_r = min(val1, val2), max(val1, val2)
                if direction == "R":
                    left_dir, right_dir = prev_dir, next_dir
                else:
                    left_dir, right_dir = opposite_dir[next_dir], opposite_dir[prev_dir]

                if left_dir == "U" and right_dir == "D":
                    cov = (val_l + 1, val_r)
                    bas = (val_l, val_r + 1)

                elif left_dir == "D" and right_dir == "D":
                    cov = (val_l, val_r)
                    bas = (val_l + 1, val_r + 1)

                elif left_dir == "D" and right_dir == "U":
                    cov = (val_l, val_r + 1)
                    bas = (val_l + 1, val_r)
                else:
                    cov = (val_l + 1, val_r + 1)
                    bas = (val_l, val_r)

                horizontal_members.append(Member(row_i, cov, bas))

            if direction in "UD":
                row_i += mod_map[direction] * distance

        return sorted(horizontal_members, key=lambda x: x.row)


    top_members = []
    members = get_horizontal_members()
    while members:
        member = members.pop(0)
        add_member = True
        m_base_l, m_base_r = member.base
        m_cov_l, m_cov_r = member.cover

        for top_member in top_members[::-1]:
            height = member.row - top_member.row - 1

            t_base_l, t_base_r = top_member.base
            t_cov_l, t_cov_r = top_member.cover

            left_base_in_range = t_cov_l < m_base_l < t_cov_r
            right_base_in_range = t_cov_l < m_base_r < t_cov_r

            left_match = t_cov_l == m_base_l
            right_match = t_cov_r == m_base_r

            if (left_match and right_match) or (left_base_in_range and right_base_in_range):
                add_member = False
                area += height * (m_base_r - m_base_l)
                top_members.remove(top_member)

                if not (left_match and right_match):
                    top_members.append(Member(top_member.row, (t_cov_l, m_base_l), (float("inf"), float("inf"))))
                    top_members.append(Member(top_member.row, (m_base_r, t_cov_r), (float("inf"), float("inf"))))

            elif not left_base_in_range and (right_base_in_range or right_match):
                add_member = False
                area += height * (m_base_r - t_cov_l)
                top_members.remove(top_member)

                if not right_match:
                    top_members.append(Member(top_member.row, (m_base_r, t_cov_r), (float("inf"), float("inf"))))

            elif (left_base_in_range or left_match) and not right_base_in_range:
                add_member = False
                area += height * (t_cov_r - m_base_l)
                top_members.remove(top_member)

                if not left_match:
                    top_members.append(Member(top_member.row, (t_cov_l, m_base_l), (float("inf"), float("inf"))))

            elif m_base_l < t_cov_l < m_base_r and m_base_l < t_cov_r < m_base_r:
                add_member = False
                area += height * (t_cov_r - t_cov_l)
                top_members.remove(top_member)

        if add_member:
            top_members.append(member)
        top_members.sort(key=lambda x: x.row)

    if plan_i == 0:
        print(f"Part1: {area}, Check is {area == 62500}")
    else:
        print(f"Part2: {area}, Check is {area == 122109860712709}")
