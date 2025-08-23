import pytest

from graphs.minimum_passes_of_matrix import (
    minimum_passes_of_matrix,
)

implementations = [minimum_passes_of_matrix]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    input = [
        [0, -1, -3, 2, 0],
        [1, -2, -5, -1, -3],
        [3, 0, 0, -4, -1],
    ]
    expected = 3
    actual = fn(input)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    input = [
        [1]
    ]
    expected = 0
    actual = fn(input)
    assert actual == expected