import pytest

from binary_trees.branch_sums import (
    branch_sums_solution_1
)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(BinaryTree):
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self
    
implementations = [branch_sums_solution_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_branch_sums_basic(fn):
    tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert fn(tree) == [15, 16, 18, 10, 11]
