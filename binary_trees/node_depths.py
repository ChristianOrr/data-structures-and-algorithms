"""
easy

The distance between a node in a Binary Tree and the tree's root is called the node's depth.

Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.

Each BinaryTree node has an integer value, a left child node, and a right child node.
Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree =    1
       /     \
      2       3
    /   \   /   \
   4     5 6     7
 /   \
8     9
Sample Output
16
// The depth of the node with value 2 is 1.
// The depth of the node with value 3 is 1.
// The depth of the node with value 4 is 2.
// The depth of the node with value 5 is 2.
// Etc..
// Summing all of these depths yields 16.

Solution 1
Time Complexity: O(n), space complexity: O(h)
Strategy:
Similar to max depth.
Recursively traverse the tree using dfs.
Keep track of the current depth and depth sum.
Base case: when the node is None return the depth sum.
Add the current depth to the depth sum, then increment the current depth by 1.
Call dfs on the left and right nodes.
Return the depth sum at the end.
"""
# Solution 1
def node_depths_solution_1(root):
    return dfs(root, 0, 0)


def dfs(node, depth, depth_sum):
    if node is None:
        return depth_sum

    depth_sum += depth
    depth += 1

    depth_sum = dfs(node.left, depth, depth_sum)
    depth_sum = dfs(node.right, depth, depth_sum)

    return depth_sum



class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
