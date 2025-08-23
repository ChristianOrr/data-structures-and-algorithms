import pytest

from arrays.longest_peak import longest_peak_solution_1


implementations = [longest_peak_solution_1]


@pytest.mark.parametrize("fn", implementations)
def test_1(fn):
    array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    assert fn(array) == 6


@pytest.mark.parametrize("fn", implementations)
def test_2(fn):
    array = [5, 4, 3, 2, 1, 2, 1]
    assert fn(array) == 3


@pytest.mark.parametrize("fn", implementations)
def test_3(fn):
    array = [1, 2, 3, 3, 2, 1]
    assert fn(array) == 0


@pytest.mark.parametrize("fn", implementations)
def test_4(fn):
    array = [1, 2, 3, 2, 1, 1]
    assert fn(array) == 5


@pytest.mark.parametrize("fn", implementations)
def test_5(fn):
    array = [1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1]
    assert fn(array) == 9
