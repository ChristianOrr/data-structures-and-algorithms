import pytest

from greedy_algorithms.valid_starting_city import (
    valid_starting_city_1,
)

implementations = [valid_starting_city_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10
    expected = 4
    actual = fn(distances, fuel, mpg)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    distances = [5, 20, 20, 10, 15]
    fuel = [1, 0, 3, 0, 3]
    mpg = 10
    expected = 2
    actual = fn(distances, fuel, mpg)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_3(fn):
    distances = [5, 2, 3]
    fuel = [1, 0, 1]
    mpg = 5
    expected = 2
    actual = fn(distances, fuel, mpg)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_4(fn):
    distances = [1, 3, 10, 6, 7, 7, 2, 4]
    fuel = [1, 1, 1, 1, 1, 1, 1, 1]
    mpg = 5
    expected = 6
    actual = fn(distances, fuel, mpg)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_5(fn):
    distances = [30, 40, 10, 10, 17, 13, 50, 30, 10, 40]
    fuel = [1, 2, 0, 1, 1, 0, 3, 1, 0, 1]
    mpg = 25
    expected = 1
    actual = fn(distances, fuel, mpg)
    assert actual == expected