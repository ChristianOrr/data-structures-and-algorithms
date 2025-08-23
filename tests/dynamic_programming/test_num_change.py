import pytest

from dynamic_programming.num_change import (
    number_of_ways_to_make_change_1,
)

implementations = [number_of_ways_to_make_change_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_num_change_basic(fn):
    assert fn(6, [1, 5]) == 2


@pytest.mark.parametrize("fn", implementations)
def test_num_change_larger(fn):
    assert fn(10, [1, 5, 10, 25]) == 4
