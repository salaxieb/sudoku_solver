"""Main function for solving sudoku."""

from typing import Optional

from sudoku_solver.datatypes import Position, Task

SUDOKU_SIZE = 3


def solver(task: Task) -> Optional[Task]:  # noqa: WPS231
    """Solving given sudoku task.

    Parameters:
        task: problem we trying to solve

    Returns:
        task: Same task, but solved if solvable else None
    """
    for position, digit in task:
        if digit != 0:
            continue

        if not allowed_options(task, position):
            return None

        for option in allowed_options(task, position):
            new_task = Task(task.task)
            new_task.set_val(position, option)
            solution = solver(new_task)
            if solution is None:
                continue
            return solution
    return task


def allowed_options(
    task: Task,
    pos: Position,
) -> set:
    """Give set of allowed digits for given position.

    Parameters:
        task: problem we trying to solve
        pos: i, j coordinate of sudoku, which we examine

    Returns:
        digits (set): Set of digits, that can be put to given position
    """
    vertical = vertical_rule_allowed(task, pos)
    horizontal = horizontal_rule_allowed(task, pos)
    square = sub_square_rule_allowed(task, pos)
    return vertical.intersection(horizontal).intersection(square)


def vertical_rule_allowed(
    task: Task,
    pos: Position,
) -> set:
    """Give set of digits by vertical rule.

    Parameters:
        task: problem we trying to solve
        pos: i, j coordinate of sudoku, which we examine

    Returns:
        digits (set): Set of digits, that can be put
            to given position according this specific rule
    """
    options = set(range(1, 10))
    for row in task.task:
        if row == pos.row_id:
            continue
        options.discard(row[pos.digit_id])
    return options


def horizontal_rule_allowed(
    task: Task,
    pos: Position,
) -> set:
    """Give set of digits by horizontal rule.

    Parameters:
        task: problem we trying to solve
        pos: i, j coordinate of sudoku, which we examine

    Returns:
        digits (set): Set of digits, that can be put
            to given position according this specific rule
    """
    options = set(range(1, 10))
    for digit_id, digit in enumerate(task.task[pos.row_id]):
        if digit_id == pos.digit_id:
            continue
        options.discard(digit)
    return options


def sub_square_rule_allowed(
    task: Task,
    pos: Position,
) -> set:
    """Give set of digits by square rule.

    Parameters:
        task: problem we trying to solve
        pos: i, j coordinate of sudoku, which we examine

    Returns:
        digits (set): Set of digits, that can be put
            to given position according this specific rule
    """
    options = set(range(1, 10))
    sub_square_ver = pos.row_id // SUDOKU_SIZE
    sub_square_hor = pos.digit_id // SUDOKU_SIZE

    for vertical in range(SUDOKU_SIZE):
        vertical = vertical + sub_square_ver * SUDOKU_SIZE

        for horizontal in range(SUDOKU_SIZE):
            horizontal = horizontal + sub_square_hor * SUDOKU_SIZE
            if Position(vertical, horizontal) == pos:
                continue
            options.discard(task.get_val(Position(vertical, horizontal)))
    return options
