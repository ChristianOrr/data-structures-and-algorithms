import pytest

from binary_trees.invert_binary_tree import (
    invert_binary_tree_solution_1,
    BinaryTree,
)

implementations = [invert_binary_tree_solution_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_invert_binary_tree_basic(fn):
    tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
    invertedTree = BinaryTree(1).inverted_insert([2, 3, 4, 5, 6, 7, 8, 9])
    fn(tree)
    assert tree == invertedTree
