"""
medium

Write a function that takes in a Binary Tree and returns its diameter.
The diameter of a binary tree is defined as the length of its longest path,
even if that path doesn't pass through the root of the tree.

A path is a collection of connected nodes in a tree, where no node is connected to more than two other nodes.
The length of a path is the number of edges between the path's first node and its last node.

Each BinaryTree node has an integer value, a left child node, and a right child node.
Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree =        1
            /   \
           3     2
         /   \
        7     4
       /       \
      8         5
     /           \
    9             6
Sample Output
6 // 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6
// There are 6 edges between the
// first node and the last node
// of this tree's longest path.
"""
import unittest


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    _, diam = backtrack(tree)
    return diam


def backtrack(node, max_diam=0):

    if node is None:
        return -1, max_diam

    left_length, max_diam = backtrack(node.left, max_diam)
    left_length += 1
    right_length, max_diam = backtrack(node.right, max_diam)
    right_length += 1

    path_diam = left_length + right_length
    if path_diam > max_diam:
        max_diam = path_diam

    if left_length > right_length:
        return left_length, max_diam
    else:
        return right_length, max_diam



class TestProgram(unittest.TestCase):
    def test_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)
        root.right = BinaryTree(2)
        expected = 6
        actual = binaryTreeDiameter(root)
        self.assertEqual(actual, expected)