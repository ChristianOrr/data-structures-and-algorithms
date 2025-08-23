"""
medium

The pre-order traversal of a Binary Tree is a traversal technique that starts at the tree's root node and
visits nodes in the following order:

Current node
Left subtree
Right subtree
Given a non-empty array of integers representing the pre-order traversal of a Binary Search Tree (BST),
write a function that creates the relevant BST and returns its root node.

The input array will contain the values of BST nodes in the order in
which these nodes would be visited with a pre-order traversal.

Each BST node has an integer value, a left child node, and a right child node.
A node is said to be a valid BST node if and only if it satisfies the BST property:
its value is strictly greater than the values of every node to its left;
its value is less than or equal to the values of every node to its right;
and its children nodes are either valid BST nodes themselves or None / null.

Sample Input
preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]
Sample Output
        10
      /    \
     4      17
   /   \      \
  2     5     19
 /           /
1           18
"""
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

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


def reconstruct_bst(preOrderTraversalValues):
    head_node = BST(preOrderTraversalValues[0])
    for value in preOrderTraversalValues[1:]:
        head_node.insert(value)
    return head_node


def get_dfs_order(node, values):
    if node is None:
        return
    values.append(node.value)
    get_dfs_order(node.left, values)
    get_dfs_order(node.right, values)
    return values


