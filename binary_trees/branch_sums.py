"""
easy

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
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums_solution_1(root):
    output = []
    dfs(root, 0, output)
    return output

def dfs(node, running_sum, output):
    running_sum += node.value
    if node.left is None and node.right is None:
        output.append(running_sum)
        return

    if node.left is not None:
        dfs(node.left, running_sum, output)
    if node.right is not None:
        dfs(node.right, running_sum, output)


class BinaryTree(BinaryTree):
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