import pytest

from binary_search_trees.find_kth_largest import find_kth_largest_value_in_bst_solution_1, BST

implementations = [find_kth_largest_value_in_bst_solution_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    root = BST(15)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.left.right = BST(3)
    root.left.right = BST(5)
    root.right = BST(20)
    root.right.left = BST(17)
    root.right.right = BST(22)
    k = 3
    assert fn(root, k) == 17


@pytest.mark.parametrize("fn", implementations)
def test_2(fn):
    root = BST(18)
    assert fn(root, 1) == 18
