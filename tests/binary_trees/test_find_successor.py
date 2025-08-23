import pytest

from binary_trees.find_successor import (
    find_successor_solution_1,
    find_successor_solution_2,
    BinaryTree,
)

implementations = [find_successor_solution_1, find_successor_solution_2]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_find_successor_basic(fn):
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.parent = root
    root.right = BinaryTree(3)
    root.right.parent = root
    root.left.left = BinaryTree(4)
    root.left.left.parent = root.left
    root.left.right = BinaryTree(5)
    root.left.right.parent = root.left
    root.left.left.left = BinaryTree(6)
    root.left.left.left.parent = root.left.left
    node = root.left.right
    expected = root
    actual = fn(root, node)
    assert actual == expected
