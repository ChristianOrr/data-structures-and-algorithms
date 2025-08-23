import pytest

from famous_algorithms.kadanes_algorithm import (
    kadanes_algorithm_1,
)

implementations = [kadanes_algorithm_1]

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    assert fn([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]) == 19

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    assert fn([-1, -2, -3, -7, -8, -10]) == -1