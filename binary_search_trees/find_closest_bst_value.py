"""
easy

Write a function that takes in a Binary Search Tree (BST) and
a target integer value and returns the closest value to that target value contained in the BST.

You can assume that there will only be one closest value.

Each BST node has an integer value, a left child node, and a right child node.
A node is said to be a valid BST node if and only if it satisfies the BST property:
its value is strictly greater than the values of every node to its left;
its value is less than or equal to the values of every node to its right;
and its children nodes are either valid BST nodes themselves or None / null.

Sample Input
tree =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14
target = 12
Sample Output
13

Solution 1
Time Complexity: O(log(n)), space complexity: O(n) - n is number of nodes
Strategy:
Recursive. Keep track of the closest node while traversing the tree.
Base case: return closest node if current node is None.
Check if current node is closer than closest and update the closest value if it is.
Traverse left side if target is less than current node.
Traverse right side if target is greater than current node.
Return current node if target is equal to current node.
"""
import unittest


def findClosestValueInBst(tree, target):
    return find_closest(tree, target, tree.value)

def find_closest(node, target, closest):
    if node is None:
        return closest

    if abs(target - closest) > abs(target - node.value):
        closest = node.value

    if target > node.value:
        return find_closest(node.right, target, closest)
    elif target < node.value:
        return find_closest(node.left, target, closest)
    else:
        return closest



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestProgram(unittest.TestCase):
    def test_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        expected = 13
        actual = findClosestValueInBst(root, 12)
        self.assertEqual(expected, actual)