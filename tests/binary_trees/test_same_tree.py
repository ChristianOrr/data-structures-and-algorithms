import pytest

from binary_trees.same_tree import (
    is_same_tree_solution_1,
    TreeNode,
)

implementations = [is_same_tree_solution_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_same_tree_basic(fn):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert fn(root, root)


@pytest.mark.parametrize("fn", implementations)
def test_same_tree_diff_structure(fn):
    p = TreeNode(1)
    p.left = TreeNode(2)
    q = TreeNode(1)
    q.right = TreeNode(2)
    assert not fn(p, q)


@pytest.mark.parametrize("fn", implementations)
def test_same_tree_diff_values(fn):
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(3)
    q.right = TreeNode(2)
    assert not fn(p, q)
