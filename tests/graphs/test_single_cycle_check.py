import pytest

from graphs.single_cycle_check import (
    has_single_cycle_1,
)

implementations = [has_single_cycle_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    assert fn([2, 3, 1, -4, -4, 2]) == True

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    assert fn([1]) == True

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_3(fn):
    assert fn([]) == True

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_4(fn):
    assert fn([3, 1, -1, -3]) == False

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_5(fn):
    assert fn([5, 1, 1, -3]) == True

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_6(fn):
    assert fn([0, 1, 1]) == False