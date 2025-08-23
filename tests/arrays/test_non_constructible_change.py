import pytest

from arrays.non_constructible_change import non_constructible_change_solution_1

implementations = [non_constructible_change_solution_1]


@pytest.mark.parametrize("fn", implementations)
def test_1(fn):
    input = [5, 7, 1, 1, 2, 3, 22]
    assert fn(input) == 20


@pytest.mark.parametrize("fn", implementations)
def test_2(fn):
    assert fn([]) == 1


@pytest.mark.parametrize("fn", implementations)
def test_3(fn):
    assert fn([1, 1]) == 3
