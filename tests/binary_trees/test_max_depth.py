import pytest

from binary_trees.max_depth import (
    max_depth_solution_1,
    BinaryTree,
)

implementations = [max_depth_solution_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_max_depth_basic(fn):
    root = BinaryTree(3)
    root.left = BinaryTree(9)
    root.right = BinaryTree(20)
    root.right.left = BinaryTree(15)
    root.right.right = BinaryTree(7)
    actual = fn(root)
    assert actual == 3
