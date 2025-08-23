import pytest

from arrays.array_of_products import array_of_products_solution_1


implementations = [array_of_products_solution_1]


@pytest.mark.parametrize("fn", implementations)
def test_basic(fn):
    array = [5, 1, 4, 2]
    assert fn(array) == [8, 40, 10, 20]
