"""Custom exceptions."""


class WrongSolutionError(Exception):
    """Your solution doesn't match with given example."""


class WrongShapeError(Exception):
    """Given array has wrong shape."""


class FixedValueError(Exception):
    """This value already calculated, why change it."""
