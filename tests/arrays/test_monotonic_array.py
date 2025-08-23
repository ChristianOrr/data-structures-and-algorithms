import pytest

from arrays.monotonic_array import monotonic_array_solution_1

implementations = [monotonic_array_solution_1]


@pytest.mark.parametrize("fn", implementations)
def test_1(fn):
    array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
    assert fn(array) is True


@pytest.mark.parametrize("fn", implementations)
def test_2(fn):
    array = [2, 2, 2, 1, 4, 5]
    assert fn(array) is False


@pytest.mark.parametrize("fn", implementations)
def test_3(fn):
    assert monotonic_array_solution_1([1, 2]) is True


@pytest.mark.parametrize("fn", implementations)
def test_4(fn):
    assert fn([]) is True


@pytest.mark.parametrize("fn", implementations)
def test_5(fn):
    assert fn([7]) is True
