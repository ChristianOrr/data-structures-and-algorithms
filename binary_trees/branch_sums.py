"""
Easy

Write a function that takes in a Binary Tree and returns a list of its
branch sums ordered from leftmost branch sum to rightmost branch sum.

A branch sum is the sum of all values in a Binary Tree branch.
A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node.

Each BinaryTree node has an integer value, a left child node, and a right child node.
Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree =     1
        /     \
       2       3
     /   \    /  \
    4     5  6    7
  /   \  /
 8    9 10
Sample Output
[15, 16, 18, 10, 11]
// 15 == 1 + 2 + 4 + 8
// 16 == 1 + 2 + 4 + 9
// 18 == 1 + 2 + 5 + 10
// 10 == 1 + 3 + 6
// 11 == 1 + 3 + 7

Solution 1
Time Complexity: O(n), space complexity: O(n) - n is the nodes in the tree
Strategy:
Solve using depth-first search.
Base case: when left and right nodes are both None,
add the current value to the running sum, then append the sum to the output array and return it.
Pass through the output array and running sum to the left and right nodes if they are not None.
Return the output array at the end.
"""
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


def branch_sums_solution_1(root, branch_sums=[], branch_sum=0):
    branch_sum += root.value

    if root.left is None and root.right is None:
        branch_sums.append(branch_sum)
        return branch_sums

    if root.left is not None:
        branch_sums = branch_sums_solution_1(root.left, branch_sums, branch_sum)

    if root.right is not None:
        branch_sums = branch_sums_solution_1(root.right, branch_sums, branch_sum)
    
    return branch_sums
