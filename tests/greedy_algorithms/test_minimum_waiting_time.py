import pytest

from greedy_algorithms.minimum_waiting_time import (
    minimum_waiting_time_1,
    minimum_waiting_time_2,
)

implementations = [minimum_waiting_time_1, minimum_waiting_time_2]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    queries = [3, 2, 1, 2, 6]
    expected = 17
    actual = fn(queries)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    queries = [2, 1, 1, 1]
    expected = 6
    actual = fn(queries)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_3(fn):
    queries = [9]
    expected = 0
    actual = fn(queries)
    assert actual == expected