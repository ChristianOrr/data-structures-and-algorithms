import pytest

from dynamic_programming.max_sum_increasing_subsequence import (
    max_sum_increasing_subsequence_1,
)

implementations = [max_sum_increasing_subsequence_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_msis_basic(fn):
    assert fn([10, 70, 20, 30, 50, 11, 30]) == [110, [10, 20, 30, 50]]


@pytest.mark.parametrize("fn", implementations)
def test_msis_decreasing(fn):
    assert fn([5, 4, 3, 2, 1]) == [5, [5]]


@pytest.mark.parametrize("fn", implementations)
def test_msis_long(fn):
    assert fn([10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]) == [164, [10, 11, 14, 23, 25, 31, 50]]
