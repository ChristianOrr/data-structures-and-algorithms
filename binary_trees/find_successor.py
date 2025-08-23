"""
medium

Write a function that takes in a Binary Tree (where nodes have an additional pointer to their parent node)
as well as a node contained in that tree and returns the given node's successor.

A node's successor is the next node to be visited (immediately after the given node)
when traversing its tree using the in-order tree-traversal technique.
A node has no successor if it's the last node to be visited in the in-order traversal.

If a node has no successor, your function should return None / null.

Each BinaryTree node has an integer value, a parent node, a left child node, and a right child node.
Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree =
              1
            /   \
           2     3
         /   \
        4     5
       /
      6
node = 5
Sample Output
1
// This tree's in-order traversal order is:
// 6 -> 4 -> 2 -> 5 -> 1 -> 3
// 1 comes immediately after 5.
"""
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# Solution 1
def find_successor_solution_1(tree, node):
    successor, _ = backtrack(tree, node)
    return successor

def backtrack(tree, node):
    if tree is None:
        return None, False

    left_value, next_parent = backtrack(tree.left, node)
    if left_value is not None:
        return left_value, False
    if next_parent:
        return tree, False
    if tree.value == node.value:
        leftmost = find_leftmost_node(tree.right)
        if leftmost is not None:
            return leftmost, False
        else:
            return None, True

    right_value, next_parent = backtrack(tree.right, node)
    if right_value is not None:
        return right_value, False
    else:
        return None, next_parent


# Solution 2
def find_successor_solution_2(tree, node):
    if tree is None:
        return None

    left_value = find_successor_solution_2(tree.left, node)
    if left_value is not None:
        return left_value

    if tree.value == node.value:
        leftmost = find_leftmost_node(tree.right)
        if leftmost is not None:
            return leftmost
        else:
            return find_leftmost_parent(node.parent)

    right_value = find_successor_solution_2(tree.right, node)
    return right_value



def find_leftmost_parent(node):
    if node is None:
        return None

    if node.parent is not None and node.parent.left.value == node.value:
        return node.parent
    parent = find_leftmost_parent(node.parent)
    if parent is None:
        return node


def find_leftmost_node(tree):
    if tree is None:
        return None
    leftmost = find_leftmost_node(tree.left)
    if leftmost is None:
        return tree
    else:
        return leftmost
