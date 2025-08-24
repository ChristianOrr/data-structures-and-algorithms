import pytest

from greedy_algorithms.tandem_bicycle import (
    tandem_bicycle_1,
)

implementations = [tandem_bicycle_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    redShirtSpeeds = [5, 5, 3, 9, 2]
    blueShirtSpeeds = [3, 6, 7, 2, 1]
    fastest = True
    expected = 32
    actual = fn(redShirtSpeeds, blueShirtSpeeds, fastest)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    redShirtSpeeds = [9]
    blueShirtSpeeds = [1]
    fastest = True
    expected = 9
    actual = fn(redShirtSpeeds, blueShirtSpeeds, fastest)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_3(fn):
    redShirtSpeeds = [5, 4, 3, 2, 1]
    blueShirtSpeeds = [1, 2, 3, 4, 5]
    fastest = False
    expected = 15
    actual = fn(redShirtSpeeds, blueShirtSpeeds, fastest)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_4(fn):
    redShirtSpeeds = [5, 4, 3, 2, 1]
    blueShirtSpeeds = [1, 2, 3, 4, 5]
    fastest = True
    expected = 21
    actual = fn(redShirtSpeeds, blueShirtSpeeds, fastest)
    assert actual == expected