import pytest

from famous_algorithms.djikstras_algorithm import (
    dijkstras_algorithm_1,
)

implementations = [dijkstras_algorithm_1]

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    start = 0
    edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
    expected = [0, 7, 13, 27, 10, -1]
    actual = fn(start, edges)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    start = 3
    edges = [[[2, 4]], [[0, 2]], [[1, 1], [3, 2]], [[0, 3]]]
    expected = [3, 8, 7, 0]
    actual = fn(start, edges)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_3(fn):
    start = 2
    edges = [[], [], [], []]
    expected = [-1, -1, 0, -1]
    actual = fn(start, edges)
    assert actual == expected