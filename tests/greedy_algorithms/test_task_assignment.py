import pytest

from greedy_algorithms.task_assignment import (
    task_assignment_1,
)

implementations = [task_assignment_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    k = 3
    tasks = [1, 3, 5, 3, 1, 4]
    expected1 = set([frozenset([4, 2]), frozenset([0, 5]), frozenset([3, 1])])
    expected2 = set([frozenset([3, 1]), frozenset([5, 4]), frozenset([2, 0])])
    actual = fn(k, tasks)
    assert actual == expected1 or actual == expected2

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    k = 1
    tasks = [3, 5]
    expected1 = set([frozenset([0, 1])])
    actual = fn(k, tasks)
    assert actual == expected1

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_3(fn):
    k = 5
    tasks = [3, 7, 5, 4, 4, 3, 6, 8, 3, 3]
    expected1 = set([frozenset([4, 3]), frozenset([2, 9]), frozenset([6, 8]), frozenset([1, 5]), frozenset([7, 0])])
    expected2 = set([frozenset([9, 7]), frozenset([8, 1]), frozenset([5, 6]), frozenset([0, 2]), frozenset([4, 3])])
    actual = fn(k, tasks)
    assert actual == expected1 or actual == expected2