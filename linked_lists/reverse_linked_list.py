"""
hard

Write a function that takes in the head of a Singly Linked List, reverses the list in place
(i.e., doesn't create a brand new list), and returns its new head.

Each LinkedList node has an integer value as well as a next node pointing to the
next node in the list or to None / null if it's the tail of the list.

You can assume that the input Linked List will always have at least one node; in other words,
the head will never be None / null.

Sample Input
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 // the head node with value 0
Sample Output
5 -> 4 -> 3 -> 2 -> 1 -> 0 // the new head node with value 5
"""
import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    current = None
    next = head

    while next is not None:
        temp = next.next
        next.next = current
        current = next
        next = temp

    return current


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
    def test_case_1(self):
        test = LinkedList(0).addMany([1, 2, 3, 4, 5])
        result = reverseLinkedList(test).getNodesInArray()
        expected = LinkedList(5).addMany([4, 3, 2, 1, 0]).getNodesInArray()
        self.assertEqual(result, expected)