"""
medium

Write a function that takes in a Binary Search Tree (BST) and
a positive integer k and returns the kth largest integer contained in the BST.

You can assume that there will only be integer values in the BST and
that k is less than or equal to the number of nodes in the tree.

Also, for the purpose of this question, duplicate integers will be treated as distinct values.
In other words, the second largest value in a BST containing values {5, 7, 7} will be 7—not 5.

Each BST node has an integer value, a left child node, and a right child node.
A node is said to be a valid BST node if and only if it satisfies the BST property:
its value is strictly greater than the values of every node to its left;
its value is less than or equal to the values of every node to its right;
and its children nodes are either valid BST nodes themselves or None / null.

Sample Input
tree =   15
       /     \
      5      20
    /   \   /   \
   2     5 17   22
 /   \
1     3
k = 3
Sample Output
17
"""
import unittest


def findKthLargestValueInBst(tree, k):
    sorted_values = in_order_traverse(tree, [])
    sorted_values.reverse()
    kth_largest = sorted_values[k - 1]
    return kth_largest


def in_order_traverse(node, array):
    if node is None:
        return array

    array = in_order_traverse(node.left, array)
    array.append(node.value)
    array = in_order_traverse(node.right, array)

    return array



class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TestProgram(unittest.TestCase):
    def test_1(self):
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
        expected = 17
        actual = findKthLargestValueInBst(root, k)
        self.assertEqual(actual, expected)

    def test_2(self):
        root = BST(18)

        k = 1
        expected = 18
        actual = findKthLargestValueInBst(root, k)
        self.assertEqual(actual, expected)

