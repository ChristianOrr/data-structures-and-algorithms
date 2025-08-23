"""
medium

Write a function that takes in a non-empty sorted array of distinct integers, constructs a BST from the integers,
and returns the root of the BST.

The function should minimize the height of the BST.

You've been provided with a BST class that you'll have to use to construct the BST.

Each BST node has an integer value, a left child node, and a right child node.
A node is said to be a valid BST node if and only if it satisfies the BST property:
its value is strictly greater than the values of every node to its left;
its value is less than or equal to the values of every node to its right;
and its children nodes are either valid BST nodes themselves or None / null.

A BST is valid if and only if all of its nodes are valid BST nodes.

Note that the BST class already has an insert method which you can use if you want.

Sample Input
array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
Sample Output
         10
       /     \
      2      14
    /   \   /   \
   1     5 13   15
          \       \
           7      22
// This is one example of a BST with min height
// that you could create from the input array.
// You could create other BSTs with min height
// from the same array; for example:
         10
       /     \
      5      15
    /   \   /   \
   2     7 13   22
 /           \
1            14
"""
def min_height_bst(array):
    middle_index = get_middle(array)
    node = BST(array[middle_index])

    if middle_index == 0:
        node.left = None
    else:
        left_array = array[0:middle_index]
        node.left = min_height_bst(left_array)
    if middle_index == len(array) - 1:
        node.right = None
    else:
        right_array = array[middle_index + 1:]
        node.right = min_height_bst(right_array)

    return node


def get_middle(array):
    array_length = len(array)
    if array_length % 2 == 1:
        return int((array_length - 1) / 2)
    else:
        return int(array_length / 2)


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
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def in_order_traverse(tree, array):
    if tree is not None:
        in_order_traverse(tree.left, array)
        array.append(tree.value)
        in_order_traverse(tree.right, array)
    return array


def validate_bst(tree):
    return validate_bst_helper(tree, float("-inf"), float("inf"))


def validate_bst_helper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validate_bst_helper(tree.left, minValue, tree.value)
    return leftIsValid and validate_bst_helper(tree.right, tree.value, maxValue)


def get_tree_height(tree, height=0):
    if tree is None:
        return height
    leftTreeHeight = get_tree_height(tree.left, height + 1)
    rightTreeHeight = get_tree_height(tree.right, height + 1)
    return max(leftTreeHeight, rightTreeHeight)

