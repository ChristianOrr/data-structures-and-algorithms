import pytest

from graphs.cycle_in_graph import (
    cycle_in_graph_1,
)

implementations = [cycle_in_graph_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    input = [[1], [2], [0]]
    expected = True
    actual = fn(input)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    input = [[]]
    expected = False
    actual = fn(input)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_3(fn):
    input = [[0]]
    expected = True
    actual = fn(input)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_4(fn):
    input = [[1, 2], [2], []]
    expected = False
    actual = fn(input)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_5(fn):
    input = [[1, 2], [2], [1]]
    expected = True
    actual = fn(input)
    assert actual == expected