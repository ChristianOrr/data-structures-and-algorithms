import pytest

from binary_search_trees.same_bsts import same_bsts


def test_same_bsts_basic():
    array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
    array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]
    assert same_bsts(array_one, array_two) is True
