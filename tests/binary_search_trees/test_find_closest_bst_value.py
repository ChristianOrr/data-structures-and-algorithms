import pytest

from binary_search_trees.find_closest_bst_value import find_closest_value_in_bst_solution_1, BST


implementations = [find_closest_value_in_bst_solution_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_example(fn):
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)

    assert fn(root, 12) == 13
