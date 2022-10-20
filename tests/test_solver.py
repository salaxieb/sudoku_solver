"""Module to test general solution."""
import pytest

from sudoku_solver.datatypes import Position, Task
from sudoku_solver.exceptions import WrongSolutionError
from sudoku_solver.sudoku_solver import solver
from tests import fixtures as fx


@pytest.mark.parametrize('task, solution', fx.examples)
def test_solver(task, solution):
    """Test solution correctness.

    Parameters:
        task: Given sudoku example
        solution: Correct solution

    Raises:
        WrongSolutionError: if my_solution != correct_solution
    """
    my_solution = solver(Task(task))
    print('my_solution', my_solution)
    if solution and my_solution != Task(solution):
        raise WrongSolutionError('Oops, check you algorithm!')

    if solution is None:
        assert my_solution is None


# @pytest.mark.parametrize('task, position, allowed, allowed_function', fx.rules)
# def test_all_allowed(task, position, allowed, allowed_function):
#     """Test total allowed functions correctness.

#     Parameters:
#         task: Given sudoku example
#         position: examined position
#         allowed: set of digit which we should get
#         allowed_function: examined function

#     Raises:
#         ValueError: if obtained value != precalculated values
#     """
#     if allowed != allowed_function(Task(task), Position(*position)):
#         raise ValueError(
#             '{f_name} works wrong'.format(f_name=allowed_function.__name__),
#         )
