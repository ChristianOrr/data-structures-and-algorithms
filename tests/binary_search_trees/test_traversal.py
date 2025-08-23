import pytest

from binary_search_trees.traversal import (
    in_order_traverse_solution_1,
    pre_order_traverse_solution_1,
    post_order_traverse_solution_1,
    BST,
)


def test_traversals():
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.right = BST(22)

    inOrder = [1, 2, 5, 5, 10, 15, 22]
    preOrder = [10, 5, 2, 1, 5, 15, 22]
    postOrder = [1, 2, 5, 5, 22, 15, 10]

    assert in_order_traverse_solution_1(root, []) == inOrder
    assert pre_order_traverse_solution_1(root, []) == preOrder
    assert post_order_traverse_solution_1(root, []) == postOrder
