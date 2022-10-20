"""Main function for solving sudoku."""

from typing import Optional

from sudoku_solver.datatypes import Position, Task
from sudoku_solver.candidates import allowed_options


def solver(task: Task, depth=0) -> Optional[Task]:
    """Solving given sudoku task.

    Parameters:
        task: problem we trying to solve

    Returns:
        task: Same task, but solved if solvable else None
    """

    min_options = 10
    min_pos = Position(0, 0)

    for position, digit in task:
        if digit == 0:
            options = allowed_options(task, position)
            if not options:
                return None
            if len(options) < min_options:
                min_options = len(options)
                min_pos = position
                
            print(depth, min_options)
            for option in allowed_options(task, min_pos):
                # new_task = Task(task.task)
                # new_task.set_val(min_pos, option)
                task.set_val(min_pos, option)
                # solution = solver(new_task, depth+1)
                solution = solver(task, depth+1)
                if solution is None:
                    task.set_val(min_pos, 0)
                    continue
                return solution
            return None
    return task
