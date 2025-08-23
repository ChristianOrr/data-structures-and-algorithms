import pytest

from dynamic_programming.traverse_graph import (
    number_of_ways_to_traverse_graph_1,
)

implementations = [number_of_ways_to_traverse_graph_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_traverse_basic(fn):
    assert fn(4, 3) == 10


@pytest.mark.parametrize("fn", implementations)
def test_traverse_larger(fn):
    assert fn(8, 5) == 330


@pytest.mark.parametrize("fn", implementations)
def test_traverse_small(fn):
    assert fn(3, 2) == 3
