"""
easy

Write a function that takes in a Binary Tree and inverts it.
In other words, the function should swap every left node in the tree for its corresponding right node.

Each BinaryTree node has an integer value, a left child node, and
a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree =    1
       /     \
      2       3
    /   \   /   \
   4     5 6     7
 /   \
8     9
Sample Output
       1
    /     \
   3       2
 /   \   /   \
7     6 5     4
            /   \
           9     8

Solution 1
Time Complexity: O(n), space complexity: O(n)
Strategy:
Recursion. Alter the tree in-place.
Swap the left and right tree nodes,
then call dfs on the left and right nodes to recursively swap the children nodes.
No need to return anything as the tree was altered in-place.

Solution 2
Time Complexity: O(n), space complexity: O(n)
Strategy:
Iterative. Alter the tree in place.
Create a queue and initialize it with the root node.
Iterate over the queue's elements while it is not empty.
Set the current node to the node at the front of the queue.
Swap the current nodes left and right nodes,
then add the left and right nodes to the back of the queue.
No need to return anything as the tree was altered in-place.

Video:
https://www.youtube.com/watch?v=OnSn2XEQ4MY&ab_channel=NeetCode
"""
def invert_binary_tree_solution_1(tree):
    swap_nodes(tree)
    return tree

def swap_nodes(node):
    if node is None:
        return

    temp = node.right
    node.right = node.left
    node.left = temp

    swap_nodes(node.left)
    swap_nodes(node.right)


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.__dict__ == other.__dict__

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

    def inverted_insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
        self.inverted_insert(values, i + 1)
        return self