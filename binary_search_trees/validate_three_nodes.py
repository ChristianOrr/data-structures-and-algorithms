"""
hard

You're given three nodes that are contained in the same Binary Search Tree: nodeOne, nodeTwo, and nodeThree.
Write a function that returns a boolean representing whether one of nodeOne or nodeThree is an ancestor of nodeTwo and
the other node is a descendant of nodeTwo.
For example, if your function determines that nodeOne is an ancestor of nodeTwo,
then it needs to see if nodeThree is a descendant of nodeTwo.
If your function determines that nodeThree is an ancestor, then it needs to see if nodeOne is a descendant.

A descendant of a node N is defined as a node contained in the tree rooted at N.
A node N is an ancestor of another node M if M is a descendant of N.

It isn't guaranteed that nodeOne or nodeThree will be ancestors or descendants of nodeTwo,
but it is guaranteed that all three nodes will be unique and will never be None / null.
In other words, you'll be given valid input nodes.

Each BST node has an integer value, a left child node, and a right child node.
A node is said to be a valid BST node if and only if it satisfies the BST property:
its value is strictly greater than the values of every node to its left;
its value is less than or equal to the values of every node to its right;
and its children nodes are either valid BST nodes themselves or None / null.

Sample Input
tree =    5
       /     \
      2       7
    /   \   /   \
   1     4 6     8
  /     /
 0     3
// This tree won't actually be passed as an input; it's here to help you visualize the problem.
nodeOne = 5 // The actual node with value 5.
nodeTwo = 2 // The actual node with value 2.
nodeThree = 3 // The actual node with value 3.
Sample Output
true // nodeOne is an ancestor of nodeTwo, and nodeThree is a descendant of nodeTwo.
"""
import unittest


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    found1 = find_node(nodeTwo, nodeOne)
    found3 = find_node(nodeTwo, nodeThree)

    if not found1 and not found3:
        return False
    elif found1:
        return find_node(nodeThree, nodeTwo)
    elif found3:
        return find_node(nodeOne, nodeTwo)


def find_node(descendant, parent):
    if parent.left is None and parent.right is None:
        return False

    if parent.left is not None:
        if parent.left.value == descendant.value:
            return True
        found_left = find_node(descendant, parent.left)
        if found_left:
            return True

    if parent.right is not None:
        if parent.right.value == descendant.value:
            return True
        found_right = find_node(descendant, parent.right)
        if found_right:
            return True

    return False


class TestProgram(unittest.TestCase):
    def test_1(self):
        root = BST(5)
        root.left = BST(2)
        root.right = BST(7)
        root.left.left = BST(1)
        root.left.right = BST(4)
        root.right.left = BST(6)
        root.right.right = BST(8)
        root.left.left.left = BST(0)
        root.left.right.left = BST(3)

        nodeOne = root
        nodeTwo = root.left
        nodeThree = root.left.right.left
        expected = True
        actual = validateThreeNodes(nodeOne, nodeTwo, nodeThree)
        self.assertEqual(actual, expected)
