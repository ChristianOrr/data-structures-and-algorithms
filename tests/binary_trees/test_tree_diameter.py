import pytest

from binary_trees.tree_diameter import (
    binary_tree_diameter_solution_1,
    BinaryTree,
)

implementations = [binary_tree_diameter_solution_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_tree_diameter_basic(fn):
    root = BinaryTree(1)
    root.left = BinaryTree(3)
    root.left.left = BinaryTree(7)
    root.left.left.left = BinaryTree(8)
    root.left.left.left.left = BinaryTree(9)
    root.left.right = BinaryTree(4)
    root.left.right.right = BinaryTree(5)
    root.left.right.right.right = BinaryTree(6)
    root.right = BinaryTree(2)
    expected = 6
    actual = fn(root)
    assert actual == expected
