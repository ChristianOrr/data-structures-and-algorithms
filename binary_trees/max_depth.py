"""
easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.

Sample Input
tree =    3
       /     \
      9       20
            /   \
          15     7

Sample Output
3

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Solution 1
Time Complexity: O(n), space complexity: O(h)
Strategy:
Similar to sum node depths problem.
Recursively traverse the tree using dfs.
Keep track of the current depth and max depth.
Base case: when the node is None return the max depth.
Increment the current depth by 1, then update max depth with the max of max depth and current depth.
Call dfs on the left and right nodes.
Return the max depth at the end.

Video:
https://www.youtube.com/watch?v=hTM3phVI6YQ&lc=UgxUajmaDDsmZ5Tp0U54AaABAg&ab_channel=NeetCode
"""
# Solution
def max_depth_solution_1(root, depth=0, max_depth=0):
    if root is None:
        return max_depth

    depth += 1
    max_depth = max(depth, max_depth)

    max_depth = max_depth_solution_1(root.left, depth, max_depth)
    max_depth = max_depth_solution_1(root.right, depth, max_depth)

    return max_depth



class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


