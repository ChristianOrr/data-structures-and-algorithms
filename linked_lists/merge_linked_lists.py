"""
easy

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

Solution 1
Time Complexity: O(n + m), space complexity: O(1)
Strategy:
Traverse both linked lists using three pointers, list1, list2 and prev. Merge list2 into list1.
While both lists have not reached the end, check if list1's value is less than list2's value.
If list1 is less than list2, then shift list1 and prev,
else link prev to list2 and shift prev onto list2, then shift list2, then link prev back to list1.
If list1 completes before list2, then link prev to list2.
Then return the list1 head.

Video:
https://www.youtube.com/watch?v=XIdigk956u0&ab_channel=NeetCode
"""
import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Solution 1
def mergeLinkedLists(headOne, headTwo):
    head = LinkedList(None)
    prev = head
    list1 = headOne
    list2 = headTwo
    prev.next = list1

    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            prev = prev.next
            list1 = list1.next
        else:
            prev.next = list2
            prev = prev.next
            list2 = list2.next
            prev.next = list1

    if list1 is None:
        prev.next = list2

    return head.next


# def mergeLinkedLists(headOne, headTwo):
#
#     if headOne.value > headTwo.value:
#         main = headTwo
#         secondary = headOne
#     else:
#         main = headOne
#         secondary = headTwo
#
#     head = main
#     while main.next is not None and secondary is not None:
#         if secondary.value < main.next.value:
#             temp = main.next
#             secondary_temp = secondary.next
#             main.next = secondary
#             main.next.next = temp
#             secondary = secondary_temp
#         main = main.next
#
#     if secondary is not None:
#         main.next = secondary
#     return head



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
        list1 = LinkedList(2).addMany([6, 7, 8])
        list2 = LinkedList(1).addMany([3, 4, 5, 9, 10])
        output = mergeLinkedLists(list1, list2)
        expectedNodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(output.getNodesInArray(), expectedNodes)

    def test_2(self):
        list1 = LinkedList(1)
        list2 = LinkedList(0)
        output = mergeLinkedLists(list1, list2)
        expectedNodes = [0, 1]
        self.assertEqual(output.getNodesInArray(), expectedNodes)

    def test_3(self):
        list1 = LinkedList(1)
        list2 = LinkedList(2)
        output = mergeLinkedLists(list1, list2)
        expectedNodes = [1, 2]
        self.assertEqual(output.getNodesInArray(), expectedNodes)