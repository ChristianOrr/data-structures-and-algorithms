import pytest

from greedy_algorithms.class_photos import (
    class_photos_1,
)

implementations = [class_photos_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    redShirtHeights = [5, 8, 1, 3, 4]
    blueShirtHeights = [6, 9, 2, 4, 5]
    expected = True
    actual = fn(redShirtHeights, blueShirtHeights)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    redShirtHeights = [6, 9, 2, 4, 5, 1]
    blueShirtHeights = [5, 8, 1, 3, 4, 9]
    expected = False
    actual = fn(redShirtHeights, blueShirtHeights)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_3(fn):
    redShirtHeights = [5, 4]
    blueShirtHeights = [5, 6]
    expected = True
    actual = fn(redShirtHeights, blueShirtHeights)
    assert actual == expected