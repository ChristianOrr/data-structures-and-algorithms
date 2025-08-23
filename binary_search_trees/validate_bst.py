"""
medium

Write a function that takes in a potentially invalid Binary Search Tree (BST) and
returns a boolean representing whether the BST is valid.

Each BST node has an integer value, a left child node, and a right child node.
A node is said to be a valid BST node if and only if it satisfies the BST property:
its value is strictly greater than the values of every node to its left;
its value is less than or equal to the values of every node to its right;
and its children nodes are either valid BST nodes themselves or None / null.

A BST is valid if and only if all of its nodes are valid BST nodes.

Sample Input
tree =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14
Sample Output
true
"""
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validate_bst(tree, max_left=None, min_right=None):
    if max_left is None:
        left_range = [-float("inf"), tree.value]
    else:
        left_range = [max_left, tree.value]
    if min_right is None:
        right_range = [tree.value, float("inf")]
    else:
        right_range = [tree.value, min_right]

    is_left_valid = True
    is_right_valid = True
    if tree.left is not None:
        is_left_valid = validate_bst(
            tree.left,
            max_left=max_left,
            min_right=min(x for x in [min_right, tree.value] if x is not None)
        )
        # left_in_range = left_range[0] < tree.left.value and tree.left.value < left_range[1]
        left_in_range = left_range[0] <= tree.left.value < left_range[1]
        is_left_valid = is_left_valid and left_in_range
    if tree.right is not None:
        is_right_valid = validate_bst(
            tree.right,
            max_left=max(x for x in [max_left, tree.value] if x is not None),
            min_right=min_right
        )
        # valid_right_list = list(range(right_range[0], right_range[1]))
        right_in_range = right_range[0] <= tree.right.value < right_range[1]
        is_right_valid = is_right_valid and right_in_range

    return is_left_valid and is_right_valid

