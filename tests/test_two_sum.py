import pytest

from arrays.two_sum import (
	two_number_sum_1,
	two_number_sum_2,
	two_number_sum_3,
)


implementations = [two_number_sum_1, two_number_sum_2, two_number_sum_3]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_basic_cases(fn):
	output = fn([3, 5, -4, 8, 11, 1, -1, 6], 10)
	assert len(output) == 2
	assert 11 in output
	assert -1 in output


@pytest.mark.parametrize("fn", implementations)
def test_single_element(fn):
	output = fn([4], 4)
	assert len(output) == 0


@pytest.mark.parametrize("fn", implementations)
def test_another_pair(fn):
	output = fn([4, 6, 1], 5)
	assert len(output) == 2
	assert 4 in output
	assert 1 in output
