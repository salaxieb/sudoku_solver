"""Keep wide used instances in standard way."""
from dataclasses import dataclass
from typing import List

from pydantic import validator

from sudoku_solver.exceptions import FixedValueError, WrongShapeError

SUDOKU_SIZE = 9


@dataclass
class Position(object):
    """Storing position in solution."""

    row_id: int
    digit_id: int

    @validator('row_id')
    def row_id_must_be_in_limits(cls, row_id):  # noqa: N805
        """Validate values row_id.

        Parameters:
            row_id: index of problem row

        Returns:
            row_id: same input row_id

        Raises:
            ValueError: if row_id not in [0, 8]
        """
        if not isinstance(row_id, int) or row_id < 0 or row_id > 8:
            raise ValueError('row_id must positive integer < 9')
        return row_id

    @validator('digit_id')
    def digit_id_must_be_in_limits(cls, digit_id):  # noqa: N805
        """Validate values row_id.

        Parameters:
            digit_id: index of problem row

        Returns:
            digit_id: same input row_id

        Raises:
            ValueError: if digit_id not in [0, 8]
        """
        if not isinstance(digit_id, int) or digit_id < 0 or digit_id > 8:
            raise ValueError('digit_id must positive integer < 9')
        return digit_id


@dataclass
class Task(object):
    """Serializer for sudoku task."""

    task: List[List[int]]

    def __init__(self, task: List[List[int]]) -> None:  # noqa: WPS231
        """Values must be valid and create a copy of mutable type.

        Parameters:
            task: 2D array shape (9, 9) representing sudoku problem

        Raises:
            WrongShapeError: raises error array not valid shape
            ValueError: if value in array not int ot not in [0, 9]
        """
        if len(task) != SUDOKU_SIZE:
            raise WrongShapeError('Array must be 9x9')

        for row in task:
            if len(row) != SUDOKU_SIZE:
                raise WrongShapeError('Array must be 9x9')

            for number in row:
                if not isinstance(number, int) or number < 0 or number > 9:
                    raise ValueError('number must positive integer <= 9')
        self.task = [list(sub_row) for sub_row in task]

    def __iter__(self):
        """Iterate sudoku position and values.

        Yields:
            Position: current iter position
            digit: value in sudoku for given position
        """
        for row_id, row in enumerate(self.task):
            for digit_id, digit in enumerate(row):  # noqa: WPS526
                yield Position(row_id, digit_id), digit

    def __repr__(self):
        """Print values beautifully.

        Returns:
            output: beautifully aligned problem.
        """
        output = '\nTask\n'
        output += '\n'.join([str(row) for row in self.task])
        return output

    def get_val(self, pos: Position) -> int:
        """Give value for given position.

        Parameters:
            pos: examined position

        Returns:
            val (int): value on given position
        """
        return self.task[pos.row_id][pos.digit_id]

    def set_val(self, pos: Position, digit: int) -> None:
        """Set value for given position.

        Parameters:
            pos: position to set value
            digit: value we set to given position

        Raises:
            FixedValueError: if we try to change value, which is fixed
            ValueError: if given value not in [0, 9]
        """
        if self.task[pos.row_id][pos.digit_id] != 0:
            raise FixedValueError('you setting value which is fixed')
        if not isinstance(digit, int) or digit < 0 or digit > 9:
            raise ValueError('value must be integer in [0, 9]')

        self.task[pos.row_id][pos.digit_id] = digit
