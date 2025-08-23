import pytest

from binary_trees.height_balanced import (
    height_balanced_binary_tree_solution_1,
    BinaryTree,
)

implementations = [height_balanced_binary_tree_solution_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_height_balanced_basic(fn):
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.right = BinaryTree(6)
    root.left.right.left = BinaryTree(7)
    root.left.right.right = BinaryTree(8)
    expected = True
    actual = fn(root)
    assert actual == expected
