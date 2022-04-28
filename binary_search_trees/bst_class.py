"""
medium

Write a BST class for a Binary Search Tree. The class should support:

Inserting values with the insert method.
Removing values with the remove method; this method should only remove the first instance of a given value.
Searching for values with the contains method.
Note that you can't remove values from a single-node tree.
In other words, calling the remove method on a single-node tree should simply not do anything.

Each BST node has an integer value, a left child node, and a right child node.
A node is said to be a valid BST node if and only if it satisfies the BST property:
its value is strictly greater than the values of every node to its left;
its value is less than or equal to the values of every node to its right;
and its children nodes are either valid BST nodes themselves or None / null.

Sample Usage
// Assume the following BST has already been created:
         10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14

// All operations below are performed sequentially.
insert(12):   10
            /     \
           5      15
         /   \   /   \
        2     5 13   22
      /        /  \
     1        12  14

remove(10):   12
            /     \
           5      15
         /   \   /   \
        2     5 13   22
      /           \
     1            14

contains(15): true
"""
import unittest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)

        elif value >= self.value:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)

        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def remove(self, value):
        if self.value == value:
            if self.left is None and self.right is None:
                self = None
            elif self.left is None:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
            elif self.right is None:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
            else:
                self.value = self.find_replacement(self.right)
                self.right = self.right.remove(self.value)

        elif value < self.value:
            self.left = self.left.remove(value)
        elif value > self.value:
            self.right = self.right.remove(value)

        return self

    def find_replacement(self, current_node):
        if current_node.left is None:
            return current_node.value
        return self.find_replacement(current_node.left)




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

        root.insert(12)
        self.assertTrue(root.right.left.left.value == 12)

        root.remove(10)
        self.assertTrue(not root.contains(10))
        self.assertTrue(root.value == 12)
        self.assertTrue(not root.right.left.left == 12)

        self.assertTrue(root.contains(15))

    def test_2(self):
        root = BST(10)

        root.insert(5)
        self.assertTrue(root.left.value == 5)
        root.insert(15)
        self.assertTrue(root.right.value == 15)

        root.remove(10)
        self.assertTrue(not root.contains(10))
        self.assertTrue(root.right is None)
        self.assertTrue(root.value == 15)
        root.remove(5)
        self.assertTrue(not root.contains(5))

    def test_3(self):
        root = BST(1)

        root.insert(2)
        self.assertTrue(root.right.value == 2)
        root.insert(3)
        self.assertTrue(root.right.right.value == 3)
        root.insert(4)
        self.assertTrue(root.right.right.right.value == 4)

        root.remove(1)
        self.assertTrue(not root.contains(1))
        self.assertTrue(root.value == 2)

