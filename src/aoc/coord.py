from typing import Dict, List


class Coord:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def straight_line(self, other):
        if self.row == other.row or self.col == other.col:
            return self.orthogonal_line(other)

        if abs(self.row - other.row) == abs(self.col - other.col):
            return self.diagonal_line(other)

        return []

    def orthogonal_line(self, other):
        if not (self.row == other.row or self.col == other.col):
            raise AssertionError(f"The coordinates are not orthogonally aligned: {self}, {other}")

        if self.row == other.row:
            return [Coord(self.row, col) for col in range(min(self.col, other.col), max(self.col, other.col) + 1)]

        if self.col == other.col:
            return [Coord(row, self.col) for row in range(min(self.row, other.row), max(self.row, other.row) + 1)]

    def diagonal_line(self, other):
        if abs(self.row - other.row) != abs(self.col - other.col):
            raise AssertionError(f"The coordinates are not diagonally aligned: {self}, {other}")

        coords_sorted = sorted([self, other], key=lambda coord: coord.col)
        col_range = range(coords_sorted[0].col, coords_sorted[1].col + 1)

        if coords_sorted[0].row > coords_sorted[1].row:
            row_range = range(coords_sorted[0].row, coords_sorted[1].row - 1, -1)
        else:
            row_range = range(coords_sorted[0].row, coords_sorted[1].row + 1)

        return [Coord(row, col) for row, col in zip(row_range, col_range)]

    def get_adjacent(self):
        top = self + Coord(-1, 0)
        bot = self + Coord(1, 0)
        lft = self + Coord(0, -1)
        rgt = self + Coord(0, 1)
        return [top, bot, lft, rgt]

    def get_surrounding(self):
        top_left = self + Coord(-1, -1)
        bot_right = self + Coord(1, 1)
        bot_lft = self + Coord(1, -1)
        top_rgt = self + Coord(-1, 1)
        coords = self.get_adjacent()
        coords.extend([top_left, bot_right, bot_lft, top_rgt])
        return coords

    def get_valid_adjacent(self, conditions: List[callable]):
        """
        Only return valid neighbors by applying a set of conditions

        example:
        conditions = [
            lambda coord: coord in map_data,
            lambda coord: coord not in visited,
            lambda coord: map_data[c_coord] < map_data[coord] < 9
        ]
        """
        return [coord for coord in self.get_adjacent() if all(condition(coord) for condition in conditions)]

    def get_valid_surrounding(self, conditions: List[callable]):
        """See get valid adjacent"""
        return [coord for coord in self.get_surrounding() if all(condition(coord) for condition in conditions)]

    def mid(self, other):
        return Coord(int((self.row + other.row) / 2), int((self.col + other.col) / 2))

    def orthogonal_distance(self, other):
        return abs(self.row - other.row) + abs(self.col - other.col)

    def distance(self, other):
        return ((self.row - other.row) ** 2 + (self.col - other.col) ** 2) ** (1 / 2)

    def __lt__(self, other):
        if self.row < other.row:
            return True
        elif self.row == other.row:
            return self.col < other.row
        else:
            return False

    def __add__(self, other):
        if isinstance(other, int):
            return Coord(self.row + other, self.col + other)

        if hasattr(other, "__iter__"):
            assert len(other) == 2
            return Coord(self.row + other[0], self.col + other[1])

        return Coord(self.row + other.row, self.col + other.col)

    def __sub__(self, other):
        if isinstance(other, int):
            return Coord(self.row - other, self.col - other)

        return Coord(self.row - other.row, self.col - other.col)

    def __mul__(self, other):
        if isinstance(other, int):
            return Coord(self.row * other, self.col * other)

        return Coord(self.row * other.row, self.col * other.col)

    def __repr__(self):
        return f"{(self.row, self.col)}"

    def __eq__(self, other):
        if self.row == other.row and self.col == other.col:
            return True

        return False

    def __hash__(self):
        return hash((self.row, self.col))


dir_map = {"R": Coord(0, 1), "L": Coord(0, -1), "D": Coord(1, 0), "U": Coord(-1, 0)}
adj4_coord = [Coord(-1, 0), Coord(0, 1), Coord(1, 0), Coord(0, -1)]

adj4 = [(c.row, c.col) for c in adj4_coord]
adj8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def print_coords_list(coords=List[Coord]):
    max_row = max([coord.row for coord in coords])
    min_row = min([coord.row for coord in coords])
    max_col = max([coord.col for coord in coords])
    min_col = min([coord.col for coord in coords])

    for row in range(min_row, max_row + 1):
        line = ""
        for col in range(min_col, max_col + 1):
            if Coord(row, col) in coords:
                line += "#"
            else:
                line += "."
        print(line)


def print_coords_dict(coord_dict, single=False, sep=None, write=None):
    coords = [coord for coord in coord_dict.keys()]

    max_row = max([coord.row for coord in coords])
    min_row = min([coord.row for coord in coords])
    max_col = max([coord.col for coord in coords])
    min_col = min([coord.col for coord in coords])

    text = ""
    for row in range(min_row, max_row + 1):
        print_list = []
        for col in range(min_col, max_col + 1):
            if Coord(row, col) in coords:
                print_list.append(coord_dict[Coord(row, col)])
            else:
                print_list.append(".")

        if write:
            text += "".join(print_list) + "\n"
        elif sep:
            print(sep.join(print_list))
        elif single:
            print("".join(print_list))
        else:
            print(print_list)

    if write:
        with open(write, "w") as f:
            f.write(text)


if __name__ == "__main__":
    coord0 = Coord(0, 0)
    coord1 = Coord(1, 1)

    coord2 = Coord(3, 1)
    coord3 = Coord(1, 3)

    coord4 = Coord(3, 3)
    coord5 = Coord(0, 100)

    assert str(coord1) == "(1, 1)"
    assert coord1 + coord2 == Coord(4, 2)

    # Test orthogonal line
    assert coord1.orthogonal_line(coord2) == [Coord(1, 1), Coord(2, 1), Coord(3, 1)]
    assert coord1.orthogonal_line(coord3) == [Coord(1, 1), Coord(1, 2), Coord(1, 3)]

    # Test diagonal line
    assert coord4.diagonal_line(coord1) == [Coord(1, 1), Coord(2, 2), Coord(3, 3)]
    assert coord4.diagonal_line(coord1) == coord1.diagonal_line(coord4)

    # Test straight line
    assert coord4.straight_line(coord1) == coord1.diagonal_line(coord4)
    assert coord1.straight_line(coord2) == coord1.orthogonal_line(coord2)
    assert coord2

    # Adjacent
    assert coord0.get_adjacent() == [Coord(-1, 0), Coord(1, 0), Coord(0, -1), Coord(0, 1)]

    # Conditional adjacent
    conditions_test = [
        lambda coord: 0 <= coord.row < 10 and 0 <= coord.col < 10
    ]
    assert coord0.get_valid_adjacent(conditions_test) == [Coord(1, 0), Coord(0, 1)]

    # Surrounding
    assert coord0.get_surrounding() == [
        Coord(-1, 0), Coord(1, 0), Coord(0, -1), Coord(0, 1), Coord(-1, -1),
        Coord(1, 1), Coord(1, -1), Coord(-1, 1)
    ]

    # mid
    assert Coord(1, 1).mid(Coord(3, 1)) == Coord(2, 1)
    assert Coord(1, 1).mid(Coord(1, 3)) == Coord(1, 2)

    # orthogonal_distance
    assert Coord(0, 0).orthogonal_distance(Coord(1, 1)) == 2

    # distance
    assert Coord(0, 0).distance(Coord(3, 4)) == 5

    # Less than
    assert Coord(3, 100) < Coord(4, 0)
    assert Coord(3, 0) < Coord(3, 1)
    assert not (Coord(3, 3) < Coord(3, 2))
