import pytest

from binary_search_trees.reconstruct_bst import (
    BST,
    reconstruct_bst,
    get_dfs_order,
)


def test_reconstruct_bst_basic():
    pre_order = [10, 4, 2, 1, 3, 17, 19, 18]
    tree = BST(10)
    tree.left = BST(4)
    tree.left.left = BST(2)
    tree.left.left.left = BST(1)
    tree.left.right = BST(3)
    tree.right = BST(17)
    tree.right.right = BST(19)
    tree.right.right.left = BST(18)
    expected = get_dfs_order(tree, [])

    actual = reconstruct_bst(pre_order)
    actual_dfs_order = get_dfs_order(actual, [])
    assert actual_dfs_order == expected
