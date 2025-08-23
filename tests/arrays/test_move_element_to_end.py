import pytest

from arrays.move_element_to_end import (
    move_element_to_end_solution_1,
    move_element_to_end_solution_2,
)

implementations = [
    move_element_to_end_solution_1,
    move_element_to_end_solution_2,
]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_move_element_basic(fn):
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    toMove = 2
    output = fn(array.copy(), toMove)
    outputStart = sorted(output[0:3])
    outputEnd = output[3:]
    assert outputStart == [1, 3, 4]
    assert outputEnd == [2, 2, 2, 2, 2]


@pytest.mark.parametrize("fn", implementations)
def test_move_element_empty(fn):
    assert fn([], 3) == []
