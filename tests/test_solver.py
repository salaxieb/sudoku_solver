"""Module to test general solution."""
import pytest

from sudoku_solver.datatypes import Position, Task
from sudoku_solver.sudoku_solver import (
    allowed_options,
    horizontal_rule_allowed,
    solver,
    sub_square_rule_allowed,
    vertical_rule_allowed,
)
from tests import fixtures as fx


@pytest.mark.parametrize('task, solution', fx.examples)
def test_solver(task, solution):
    """Test solution correctness.

    Parameters
    ----------
        task: List[List[int]]
            Given sudoku example
        solution: List[List[int]]
            Correct solution
    """
    my_solution = solver(Task(task))
    assert my_solution == Task(solution)


functions = {
    'vertical': vertical_rule_allowed,
    'horizontal': horizontal_rule_allowed,
    'square': sub_square_rule_allowed,
    'total': allowed_options,
}


@pytest.mark.parametrize('task, position, allowed, rule', fx.rules)
def test_all_allowed(task, position, allowed, rule):
    """Test total allowed functions correctness."""
    allowed_function = functions.get(rule)
    if allowed != allowed_function(Task(task), Position(*position)):
        raise ValueError(
            '{f_name} works wrong'.format(f_name=allowed_function.__name__),
        )
