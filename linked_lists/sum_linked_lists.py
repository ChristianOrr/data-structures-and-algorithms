"""
medium

You're given two Linked Lists of potentially unequal length.
Each Linked List represents a non-negative integer, where each node in the Linked List is a digit of that integer, and
the first node in each Linked List always represents the least significant digit of the integer.
Write a function that returns the head of a new Linked List that represents the sum of the
integers represented by the two input Linked Lists.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or
to None / null if it's the tail of the list. The value of each LinkedList node is always in the range of 0 - 9.

Note: your function must create and return a new Linked List, and
you're not allowed to modify either of the input Linked Lists.

Sample Input
linkedListOne = 2 -> 4 -> 7 -> 1
linkedListTwo = 9 -> 4 -> 5
Sample Output
1 -> 9 -> 2 -> 2
// linkedListOne represents 1742
// linkedListTwo represents 549
// 1742 + 549 = 2291
"""
import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def create_ll(self, integer):
        if integer != "":
            self.next = LinkedList(int(integer[-1]))
            integer = integer[:-1]
            self.next.create_ll(integer)

        return self

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    integer1 = get_integer(linkedListOne)
    integer2 = get_integer(linkedListTwo)
    integer3 = integer1 + integer2
    integer3 = str(integer3)
    ll_3 = LinkedList(int(integer3[-1])).create_ll(integer3[:-1])
    return ll_3


def get_integer(linked_list):
    int_string = ""

    while linked_list is not None:
        int_string = str(linked_list.value) + int_string
        linked_list = linked_list.next
    return int(int_string)



class LinkedList(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self


def getNodesInArray(output):
    nodes = []
    current = output
    while current is not None:
        nodes.append(current.value)
        current = current.next
    return nodes


class TestProgram(unittest.TestCase):
    def test_1(self):
        ll1 = LinkedList(2).addMany([4, 7, 1])
        ll2 = LinkedList(9).addMany([4, 5])
        expected = LinkedList(1).addMany([9, 2, 2])
        actual = sumOfLinkedLists(ll1, ll2)
        self.assertEqual(getNodesInArray(actual), getNodesInArray(expected))
