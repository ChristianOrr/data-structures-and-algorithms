import pytest

from arrays.spiral_traverse import spiral_traverse_solution_1

implementations = [spiral_traverse_solution_1]


@pytest.mark.parametrize("fn", implementations)
def test_1(fn):
    matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    assert fn(matrix) == expected
