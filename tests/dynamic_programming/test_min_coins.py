import pytest

from dynamic_programming.min_coins import (
    min_number_of_coins_for_change_1,
)

implementations = [min_number_of_coins_for_change_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_min_coins_basic(fn):
    assert fn(7, [1, 5, 10]) == 3


@pytest.mark.parametrize("fn", implementations)
def test_min_coins_impossible(fn):
    assert fn(7, [2, 4]) == -1
