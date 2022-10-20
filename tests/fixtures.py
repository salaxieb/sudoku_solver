"""Test fixtures."""

from sudoku_solver.candidates import (
    allowed_options, horizontal_rule_allowed,
    sub_square_rule_allowed, vertical_rule_allowed,
)

task = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0],
]

solution = [
    [4, 3, 5, 2, 6, 9, 7, 8, 1],
    [6, 8, 2, 5, 7, 1, 4, 9, 3],
    [1, 9, 7, 8, 3, 4, 5, 6, 2],
    [8, 2, 6, 1, 9, 5, 3, 4, 7],
    [3, 7, 4, 6, 8, 2, 9, 1, 5],
    [9, 5, 1, 7, 4, 3, 6, 2, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 7, 1, 3, 6],
    [7, 6, 3, 4, 1, 8, 2, 5, 9],
]

hard_task = [
    [0, 0, 0, 7, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 3, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 5, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 1, 8],
    [0, 0, 0, 0, 8, 1, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 5, 0],
    [0, 4, 0, 0, 0, 0, 3, 0, 0],
]


non_solvable_task = [
    [0, 0, 0, 2, 6, 8, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0],
]


examples = [
    (task, solution),
    (solution, solution),
    # (hard_task, None),
    (non_solvable_task, None)
]


allowed_vertical_examples = [
    (task, (0, 0), {2, 3, 4, 5, 9}),
    (task, (8, 1), {1, 3, 6, 7}),
]

allowed_horizontal_examples = [
    (task, (0, 0), {3, 4, 5, 8, 9}),
    (task, (8, 1), {2, 4, 5, 6, 9}),
]

allowed_square_examples = [
    (task, [0, 0], {2, 3, 4, 5, 7}),
    (task, (8, 1), {1, 2, 5, 6, 8}),
]

allowed_total_examples = [
    (task, (0, 0), {3, 4, 5}),
    (task, (8, 1), {6}),
]

rules = [
    *[(*args, vertical_rule_allowed) for args in allowed_vertical_examples],
    *[
        (*args, horizontal_rule_allowed)
        for args in allowed_horizontal_examples
    ],
    *[(*args, sub_square_rule_allowed) for args in allowed_square_examples],
    *[(*args, allowed_options) for args in allowed_total_examples],
]
