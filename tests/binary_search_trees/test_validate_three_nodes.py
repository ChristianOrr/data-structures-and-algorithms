import pytest

from binary_search_trees.validate_three_nodes import (
    BST,
    validate_three_nodes,
)


def test_validate_three_nodes_basic():
    root = BST(5)
    root.left = BST(2)
    root.right = BST(7)
    root.left.left = BST(1)
    root.left.right = BST(4)
    root.right.left = BST(6)
    root.right.right = BST(8)
    root.left.left.left = BST(0)
    root.left.right.left = BST(3)

    node_one = root
    node_two = root.left
    node_three = root.left.right.left
    expected = True
    actual = validate_three_nodes(node_one, node_two, node_three)
    assert actual == expected
