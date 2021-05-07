"""Module to test general solution."""
import pytest

from sudoku_solver.datatypes import Position, Task
from sudoku_solver.sudoku_solver import solver
from tests import fixtures as fx
from tests.exceptions import WrongSolutionError


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
    if my_solution != Task(solution):
        raise WrongSolutionError('Oops, check you algorithm!')


@pytest.mark.parametrize('task, position, allowed, allowed_function', fx.rules)
def test_all_allowed(task, position, allowed, allowed_function):
    """Test total allowed functions correctness."""
    if allowed != allowed_function(Task(task), Position(*position)):
        raise ValueError(
            '{f_name} works wrong'.format(f_name=allowed_function.__name__),
        )
