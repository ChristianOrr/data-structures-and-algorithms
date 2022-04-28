"""
hard

Write a function that takes in the head of a Singly Linked List that contains a loop (in other words,
the list's tail node points to some node in the list instead of None / null).
The function should return the node (the actual node--not just its value)
from which the loop originates in constant space.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list.

Sample Input
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 // the head node with value 0
                           ^         v
                           9 <- 8 <- 7
Sample Output
4 -> 5 -> 6 // the node with value 4
^         v
9 <- 8 <- 7
"""
import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    nodes_set = set()
    node = head
    while node not in nodes_set:
        nodes_set.add(node)
        node = node.next
    return node





class LinkedList(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNthNode(self, n):
        counter = 1
        current = self
        while counter < n:
            current = current.next
            counter += 1
        return current


class TestProgram(unittest.TestCase):
    def test_1(self):
        test = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        test.getNthNode(10).next = test.getNthNode(5)
        self.assertEqual(findLoop(test), test.getNthNode(5))