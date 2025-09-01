import pytest

from arrays.validate_subsequence import (
    validate_subsequence_solution_1,
    validate_subsequence_solution_2
)


implementations = [validate_subsequence_solution_1, validate_subsequence_solution_2]


@pytest.mark.parametrize("fn", implementations)
def test_subsequence_basic(fn):
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    assert fn(array, sequence)


@pytest.mark.parametrize("fn", implementations)
def test_subsequence_single(fn):
    assert fn([5], [5])


@pytest.mark.parametrize("fn", implementations)
def test_subsequence_false(fn):
    assert not fn([5], [4])
