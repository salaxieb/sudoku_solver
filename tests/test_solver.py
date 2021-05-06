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
from tests.fixtures import examples_supplier  # noqa: F401


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


def test_all_allowed(examples_supplier):  # noqa: F811, WPS442
    """Test total allowed functions correctness."""
    task, position, allowed, rule = examples_supplier
    allowed_function = functions.get(rule)
    assert allowed == allowed_function(Task(task), Position(*position))
