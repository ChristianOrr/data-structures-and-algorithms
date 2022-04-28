"""
hard

Write a function that takes in the heads of two Singly Linked Lists that are in sorted order, respectively.
The function should merge the lists in place (i.e., it shouldn't create a brand new list) and
return the head of the merged list; the merged list should be in sorted order.

Each LinkedList node has an integer value as well as a next node pointing to the
next node in the list or to None / null if it's the tail of the list.

You can assume that the input linked lists will always have at least one node; in other words,
the heads will never be None / null.

Sample Input
headOne = 2 -> 6 -> 7 -> 8 // the head node with value 2
headTwo = 1 -> 3 -> 4 -> 5 -> 9 -> 10 // the head node with value 1
Sample Output
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 // the new head node with value 1
"""
import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):

    if headOne.value > headTwo.value:
        main = headTwo
        secondary = headOne
    else:
        main = headOne
        secondary = headTwo

    head = main
    while main.next is not None and secondary is not None:
        if secondary.value < main.next.value:
            temp = main.next
            secondary_temp = secondary.next
            main.next = secondary
            main.next.next = temp
            secondary = secondary_temp
        main = main.next

    if secondary is not None:
        main.next = secondary
    return head



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
        list1 = LinkedList(2).addMany([6, 7, 8])
        list2 = LinkedList(1).addMany([3, 4, 5, 9, 10])
        output = mergeLinkedLists(list1, list2)
        expectedNodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(output.getNodesInArray(), expectedNodes)