"""
hard

Write a function that takes in the head of a Singly Linked List and an integer k,
shifts the list in place (i.e., doesn't create a brand new list) by k positions, and returns its new head.

Shifting a Linked List means moving its nodes forward or backward and wrapping them around the list where appropriate.
For example, shifting a Linked List forward by one position would make its tail become the new head of the linked list.

Whether nodes are moved forward or backward is determined by whether k is positive or negative.

Each LinkedList node has an integer value as well as a next node pointing to the
next node in the list or to None / null if it's the tail of the list.

You can assume that the input Linked List will always have at least one node; in other words,
the head will never be None / null.

Sample Input
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 // the head node with value 0
k = 2
Sample Output
4 -> 5 -> 0 -> 1 -> 2 -> 3 // the new head node with value 4
"""
import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    if k == 0:
        return head

    num_nodes = 0
    node = head
    while node is not None:
        num_nodes += 1
        node = node.next
    if k % num_nodes == 0:
        return head

    if k < 0:
        k = num_nodes + k
    last_node = num_nodes - k % num_nodes

    node_num = 1
    node = head
    while node_num != last_node:
        node_num += 1
        node = node.next

    new_head = node.next
    node.next = None

    new_node = new_head
    while new_node.next is not None:
        new_node = new_node.next

    new_node.next = head

    return new_head




def linkedListToArray(head):
    array = []
    current = head
    while current is not None:
        array.append(current.value)
        current = current.next
    return array


class TestProgram(unittest.TestCase):
    def test_1(self):
        head = LinkedList(0)
        head.next = LinkedList(1)
        head.next.next = LinkedList(2)
        head.next.next.next = LinkedList(3)
        head.next.next.next.next = LinkedList(4)
        head.next.next.next.next.next = LinkedList(5)
        result = shiftLinkedList(head, 2)
        array = linkedListToArray(result)

        expected = [4, 5, 0, 1, 2, 3]
        self.assertEqual(expected, array)

    def test_2(self):
        head = LinkedList(0)
        head.next = LinkedList(1)
        head.next.next = LinkedList(2)
        head.next.next.next = LinkedList(3)
        head.next.next.next.next = LinkedList(4)
        head.next.next.next.next.next = LinkedList(5)
        result = shiftLinkedList(head, 6)
        array = linkedListToArray(result)

        expected = [0, 1, 2, 3, 4, 5]
        self.assertEqual(expected, array)

    def test_3(self):
        head = LinkedList(0)
        head.next = LinkedList(1)
        head.next.next = LinkedList(2)
        head.next.next.next = LinkedList(3)
        head.next.next.next.next = LinkedList(4)
        head.next.next.next.next.next = LinkedList(5)
        result = shiftLinkedList(head, -1)
        array = linkedListToArray(result)

        expected = [1, 2, 3, 4, 5, 0]
        self.assertEqual(expected, array)