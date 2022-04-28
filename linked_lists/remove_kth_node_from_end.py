"""
medium

Write a function that takes in the head of a Singly Linked List and
an integer k and removes the kth node from the end of the list.

The removal should be done in place, meaning that the original data structure should be mutated
(no new structure should be created).

Furthermore, the input head of the linked list should remain the head of the linked list after the removal is done,
even if the head is the node that's supposed to be removed.
In other words, if the head is the node that's supposed to be removed,
your function should simply mutate its value and next pointer.

Note that your function doesn't need to return anything.

You can assume that the input Linked List will always have at least two nodes and, more specifically, at least k nodes.

Each LinkedList node has an integer value as well as a next node pointing to the
next node in the list or to None / null if it's the tail of the list.

Sample Input
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 // the head node with value 0
k = 4
Sample Output
// No output required.
// The 4th node from the end of the list (the node with value 6) is removed.
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9
"""
import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    node = head
    num_nodes = 1

    while node.next is not None:
        num_nodes += 1
        node = node.next
    k_to_alter = num_nodes - k


    if k_to_alter == 0:
        head.value = head.next.value
        head.next = head.next.next
    else:
        node = head
        node_position = 1
        while node_position != k_to_alter:
            node_position += 1
            node = node.next

        node.next = node.next.next




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
        test = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected = LinkedList(0).addMany([1, 2, 3, 4, 5, 7, 8, 9])
        removeKthNodeFromEnd(test, 4)
        self.assertEqual(test.getNodesInArray(), expected.getNodesInArray())

    def test_2(self):
        test = LinkedList(0).addMany([1, 2])
        expected = LinkedList(1).addMany([2])
        removeKthNodeFromEnd(test, 3)
        self.assertEqual(test.getNodesInArray(), expected.getNodesInArray())
