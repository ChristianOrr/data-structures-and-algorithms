"""
easy

You're given a Node class that has a name and an array of optional children nodes.
When put together, nodes form an acyclic tree-like structure.

Implement the depthFirstSearch method on the Node class, which takes in an empty array,
traverses the tree using the Depth-first Search approach (specifically navigating the tree from left to right),
stores all of the nodes' names in the input array, and returns it.

Sample Input
graph = A
     /  |  \
    B   C   D
   / \     / \
  E   F   G   H
     / \   \
    I   J   K
Sample Output
["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

Solution 1
Time Complexity: O(v + e), space complexity: O(v)
Strategy:
Recursive, go deep, then wide in the tree.
Add current nodes name to the array.
Iterate over all the children and call dfs on all the children nodes.
After the loop return the array.

"""

# # Template
# class Node:
#     def __init__(self, name):
#         self.children = []
#         self.name = name
#
#     def addChild(self, name):
#         self.children.append(Node(name))
#         return self
#
#     def depthFirstSearch(self, array):
#         pass


# Solution 1
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

