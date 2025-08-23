import pytest

from arrays.sorted_squared_array import sorted_squared_array_solution_1


implementations = [sorted_squared_array_solution_1]


@pytest.mark.parametrize("fn", implementations)
def test_basic(fn):
    inp = [-3, 1, 2, 3, 5]
    assert fn(inp) == [1, 4, 9, 9, 25]
