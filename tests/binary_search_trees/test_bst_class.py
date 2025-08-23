import pytest

from binary_search_trees.bst_class import BST


def test_bst_insert_remove_contains_case_1():
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)

    root.insert(12)
    assert root.right.left.left.value == 12

    root.remove(10)
    assert not root.contains(10)
    assert root.value == 12
    assert not root.right.left.left == 12

    assert root.contains(15)


def test_bst_insert_remove_contains_case_2():
    root = BST(10)

    root.insert(5)
    assert root.left.value == 5
    root.insert(15)
    assert root.right.value == 15

    root.remove(10)
    assert not root.contains(10)
    assert root.right is None
    assert root.value == 15
    root.remove(5)
    assert not root.contains(5)


def test_bst_insert_remove_contains_case_3():
    root = BST(1)

    root.insert(2)
    assert root.right.value == 2
    root.insert(3)
    assert root.right.right.value == 3
    root.insert(4)
    assert root.right.right.right.value == 4

    root.remove(1)
    assert not root.contains(1)
    assert root.value == 2
