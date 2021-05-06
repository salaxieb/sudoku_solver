"""Keep wide used instances in standard way."""
from dataclasses import dataclass
from typing import List

from pydantic import validator


@dataclass
class Position:
    """Storing position in solution."""

    row_id: int
    digit_id: int

    @validator('row_id')
    def row_id_must_be_in_limits(cls, row_id):  # noqa: D102, N805
        if not isinstance(row_id, int) or row_id < 0 or row_id > 8:
            raise ValueError('row_id must positive integer < 9')
        return row_id

    @validator('digit_id')
    def digit_id_must_be_in_limits(cls, digit_id):  # noqa: D102, N805
        if not isinstance(digit_id, int) or digit_id < 0 or digit_id > 8:
            raise ValueError('row_id must positive integer < 9')
        return digit_id


@dataclass
class Task:
    """Serializer for sudoku task."""

    task: List[List[int]]

    def __init__(
        self,
        task: List[List[int]],
    ) -> None:
        """Values must be valid and create a copy of mutable type."""
        for row in task:
            for number in row:
                if not isinstance(number, int) or number < 0 or number > 9:
                    raise ValueError('number must positive integer <= 9')
        self.task = [list(sub_row) for sub_row in task]

    def __iter__(self):
        """Iterate sudoku position and values."""
        for row_id, row in enumerate(self.task):
            for digit_id, digit in enumerate(row):  # noqa: WPS526
                yield Position(row_id, digit_id), digit

    def __repr__(self):
        """Print values beautifully."""
        output = '\nTask\n'
        output += '\n'.join([str(row) for row in self.task])
        return output

    def get_val(self, pos: Position) -> int:
        """Give value for given position."""
        return self.task[pos.row_id][pos.digit_id]

    def set_val(self, pos: Position, digit: int) -> None:
        """Set value for given position."""
        if self.task[pos.row_id][pos.digit_id] != 0:
            raise ValueError('you setting value which is fixed')
        if not isinstance(digit, int) or digit < 0 or digit > 9:
            raise ValueError('value must be integer in [0, 9]')

        self.task[pos.row_id][pos.digit_id] = digit
