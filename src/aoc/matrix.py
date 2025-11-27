from enum import Enum


def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def reverse_matrix(matrix):
    return [row[::-1] for row in matrix]


class Direction(Enum):
    LEFT = "L"
    RIGHT = "R"


def rotate_matrix(matrix, direction):
    if direction == Direction.LEFT:
        return transpose_matrix(reverse_matrix(matrix))
    elif direction == Direction.RIGHT:
        return reverse_matrix(transpose_matrix(matrix))
    else:
        raise AssertionError("wrong direction")
