import pytest

from binary_search_trees.right_smaller_than import (
    right_smaller_than_1,
    right_smaller_than_2,
)

implementations = [right_smaller_than_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_right_smaller_than_basic(fn):
    array = [8, 5, 11, -1, 3, 4, 2]
    expected = [5, 4, 4, 0, 1, 1, 0]
    assert fn(list(array)) == expected


@pytest.mark.parametrize("fn", implementations)
def test_right_smaller_than_empty(fn):
    assert fn([]) == []
