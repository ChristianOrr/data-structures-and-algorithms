import pytest

from binary_search_trees.min_height import (
    min_height_bst,
    in_order_traverse,
    validate_bst,
    get_tree_height,
)


def test_min_height_bst_basic():
    array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    tree = min_height_bst(array)

    assert validate_bst(tree)
    assert get_tree_height(tree) == 4

    in_order = in_order_traverse(tree, [])
    assert in_order == [1, 2, 5, 7, 10, 13, 14, 15, 22]
