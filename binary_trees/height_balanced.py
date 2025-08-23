"""
medium

You're given the root node of a Binary Tree.
Write a function that returns true if this Binary Tree is height balanced and false if it isn't.

A Binary Tree is height balanced if for each node in the tree,
the difference between the height of its left subtree and the height of its right subtree is at most 1.

Each BinaryTree node has an integer value, a left child node, and a right child node.
Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree = 1
     /   \
    2     3
  /   \     \
 4     5     6
     /   \
    7     8
Sample Output
true
"""
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height_balanced_binary_tree_solution_1(tree):
    if tree is None:
        return True

    height = backtrack(tree)

    if height is None:
        return False
    else:
        return True


def backtrack(node,  height=0):
    if node is None:
        return height
    height += 1
    left_height = backtrack(node.left, height)
    right_height = backtrack(node.right, height)

    if left_height is None or right_height is None:
        return None

    if abs(left_height - right_height) > 1:
        return None
    else:
        return max(left_height, right_height)

