import pytest

from heaps.continuous_median import (
    ContinuousMedianHandler,
)

implementations = [ContinuousMedianHandler]

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_continuous_median_1(fn):
    handler = fn()
    handler.insert(5)
    handler.insert(10)
    assert handler.get_median() == 7.5
    handler.insert(100)
    assert handler.get_median() == 10

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_continuous_median_2(fn):
    handler = fn()
    handler.insert(1)
    handler.insert(2)
    handler.insert(3)
    assert handler.get_median() == 2
    handler.insert(4)
    assert handler.get_median() == 2.5

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_continuous_median_3(fn):
    handler = fn()
    handler.insert(5)
    handler.insert(1)
    handler.insert(3)
    assert handler.get_median() == 3
    handler.insert(2)
    assert handler.get_median() == 2.5