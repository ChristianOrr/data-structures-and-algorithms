import pytest

from binary_trees.branch_sums import (
    branch_sums_solution_1,
    BinaryTree,
)

implementations = [branch_sums_solution_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_branch_sums_basic(fn):
    tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert fn(tree) == [15, 16, 18, 10, 11]
