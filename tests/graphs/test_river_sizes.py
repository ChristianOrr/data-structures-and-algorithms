import pytest

from graphs.river_sizes import (
    river_sizes_1,
)

implementations = [river_sizes_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    testInput = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]
    ]
    expected = [1, 2, 2, 2, 5]
    assert sorted(fn(testInput)) == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    testInput = [
        [1, 1],
        [1, 1],
    ]
    expected = [4]
    assert sorted(fn(testInput)) == expected