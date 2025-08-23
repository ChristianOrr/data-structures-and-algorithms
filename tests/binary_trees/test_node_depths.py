import pytest

from binary_trees.node_depths import (
    node_depths_solution_1,
    BinaryTree,
)

implementations = [node_depths_solution_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_node_depths_basic(fn):
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    actual = fn(root)
    assert actual == 16
