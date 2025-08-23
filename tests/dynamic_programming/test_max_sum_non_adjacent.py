import pytest

from dynamic_programming.max_sum_non_adjacent import (
    max_subset_sum_no_adjacent_1,
)

implementations = [max_subset_sum_no_adjacent_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_msna_basic(fn):
    assert fn([75, 105, 120, 75, 90, 135]) == 330


@pytest.mark.parametrize("fn", implementations)
def test_msna_empty(fn):
    assert fn([]) == 0
