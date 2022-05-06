"""
easy

You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values.
Write a function that returns a modified version of the Linked List that
doesn't contain any nodes with duplicate values.
The Linked List should be modified in place (i.e., you shouldn't create a brand new list), and
the modified Linked List should still have its nodes sorted with respect to their values.

Each LinkedList node has an integer value as well as a next node pointing to the
next node in the list or to None / null if it's the tail of the list.

Sample Input
linkedList = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6 // the head node with value 1
Sample Output
1 -> 3 -> 4 -> 5 -> 6 // the head node with value 1

Solution 1
Time Complexity: O(n), space complexity: O(n)
Strategy:
Create set to store all the different node values.
Iterate through the linked list while the current node is not None.
Use inner while loop to slide along until you find a node that's unique (ie. not in the set).
After inner while loop let the next node = next_unique node and move onto the next node.
Return the linked list after the loop.

Solution 2
Time Complexity: O(n), space complexity: O(1)
Strategy:
Iterate through the linked list while the current node is not None.
Use inner while loop to slide along until you find a node that's unique.
After inner while loop let the next node = next_unique node and move onto the next node.
Return the linked list after the loop.
"""
import unittest

# Default class
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Solution 1
def removeDuplicatesFromLinkedList(linkedList):
    node = linkedList
    node_values = set()

    while node is not None:
        node_values.add(node.value)
        next_unique = node.next

        while next_unique is not None and next_unique.value in node_values:
            next_unique = next_unique.next

        node.next = next_unique
        node = node.next

    return linkedList


# Solution 2
def removeDuplicatesFromLinkedList(linkedList):

    node = linkedList
    while node is not None:
        next_unique = node.next
        while next_unique is not None and node.value == next_unique.value:
            next_unique = next_unique.next

        node.next = next_unique
        node = node.next

    return linkedList


# Testing classes
class LinkedList(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


class TestProgram(unittest.TestCase):
    def test_1(self):
        test = LinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
        expected = LinkedList(1).addMany([3, 4, 5, 6])
        actual = removeDuplicatesFromLinkedList(test)
        self.assertEqual(actual.getNodesInArray(), expected.getNodesInArray())