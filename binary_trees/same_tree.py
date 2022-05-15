"""
easy

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
p = q =    1
       /     \
      2       3
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
p =       1
       /
      2
q =       1
            \
             2
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
p =       1
       /    \
      2      1
q =        1
        /    \
       1      2

Input: p = [1,2,1], q = [1,1,2]
Output: false

Solution 1
Time Complexity: O(p + q), space complexity: O(p + q)
Strategy:
Use dfs to recursively traverse both trees at the same time.
Base case: Both p and q is None, return True, otherwise if only one is None return False.
Compare the current p and q nodes values,
if they are the same recursively call dfs on the left and right children.
Return True if left and right are True, otherwise return False.

Video:
https://www.youtube.com/watch?v=vRbbcKXCxOw&ab_channel=NeetCode
"""
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    return dfs(p, q)

def dfs(p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    else:
        is_left_same = dfs(p.left, q.left)
        is_right_same = dfs(p.right, q.right)
        return is_left_same and is_right_same



class TestProgram(unittest.TestCase):
    def test_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertTrue(isSameTree(root, root))

    def test_2(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        q = TreeNode(1)
        q.right = TreeNode(2)

        self.assertTrue(not isSameTree(p, q))

    def test_3(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        q = TreeNode(1)
        q.left = TreeNode(3)
        q.right = TreeNode(2)

        self.assertTrue(not isSameTree(p, q))