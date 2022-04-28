"""
medium

Write a DoublyLinkedList class that has a head and a tail,
both of which point to either a linked list Node or None / null. The class should support:

Setting the head and tail of the linked list.
Inserting nodes before and after other nodes as well as at given positions (the position of the head node is 1).
Removing given nodes and removing nodes with given values.
Searching for nodes with given values.
Note that the setHead, setTail, insertBefore, insertAfter, insertAtPosition, and
remove methods all take in actual Nodes as input parameters—not integers
(except for insertAtPosition, which also takes in an integer representing the position);
this means that you don't need to create any new Nodes in these methods.
The input nodes can be either stand-alone nodes or nodes that are already in the linked list.
If they're nodes that are already in the linked list,
the methods will effectively be moving the nodes within the linked list.
You won't be told if the input nodes are already in the linked list,
so your code will have to defensively handle this scenario.

Each Node has an integer value as well as a prev node and a next node,
both of which can point to either another node or None / null.

Sample Usage
// Assume the following linked list has already been created:
1 <-> 2 <-> 3 <-> 4 <-> 5
// Assume that we also have the following stand-alone nodes:
3, 3, 6
setHead(4): 4 <-> 1 <-> 2 <-> 3 <-> 5 // set the existing node with value 4 as the head
setTail(6): 4 <-> 1 <-> 2 <-> 3 <-> 5 <-> 6 // set the stand-alone node with value 6 as the tail
insertBefore(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 // move the existing node with value 3 before the existing node with value 6
insertAfter(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a stand-alone node with value 3 after the existing node with value 6
insertAtPosition(1, 3): 3 <-> 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a stand-alone node with value 3 in position 1
removeNodesWithValue(3): 4 <-> 1 <-> 2 <-> 5 <-> 6 // remove all nodes with value 3
remove(2): 4 <-> 1 <-> 5 <-> 6 // remove the existing node with value 2
containsNodeWithValue(5): true
"""
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)


    def setTail(self, node):
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.insertAfter(self.tail, node)


    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert


    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert



    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        current_position = 1
        while node is not None and current_position != position:
            node = node.next
            current_position += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)


    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            temp = node.next
            if node.value == value:
                self.remove(node)
            node = temp


    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        node.prev = None
        node.next = None


    def containsNodeWithValue(self, value):
        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False


class TestNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


Node = TestNode


def getNodeValuesHeadToTail(linkedList):
    values = []
    node = linkedList.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values


def getNodeValuesTailToHead(linkedList):
    values = []
    node = linkedList.tail
    while node is not None:
        values.append(node.value)
        node = node.prev
    return values


def bindNodes(nodeOne, nodeTwo):
    nodeOne.next = nodeTwo
    nodeTwo.prev = nodeOne


class TestProgram(unittest.TestCase):
    def test_1(self):
        linkedList = DoublyLinkedList()
        one = Node(1)
        two = Node(2)
        three = Node(3)
        three2 = Node(3)
        three3 = Node(3)
        four = Node(4)
        five = Node(5)
        six = Node(6)
        bindNodes(one, two)
        bindNodes(two, three)
        bindNodes(three, four)
        bindNodes(four, five)
        linkedList.head = one
        linkedList.tail = five

        linkedList.setHead(four)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 3, 5])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [5, 3, 2, 1, 4])

        linkedList.setTail(six)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 3, 5, 6])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 5, 3, 2, 1, 4])

        linkedList.insertBefore(six, three)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 5, 3, 6])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 3, 5, 2, 1, 4])

        linkedList.insertAfter(six, three2)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 5, 3, 6, 3])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 6, 3, 5, 2, 1, 4])

        linkedList.insertAtPosition(1, three3)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [3, 4, 1, 2, 5, 3, 6, 3])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 6, 3, 5, 2, 1, 4, 3])

        linkedList.removeNodesWithValue(3)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 5, 6])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 5, 2, 1, 4])

        linkedList.remove(two)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 5, 6])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 5, 1, 4])

        self.assertEqual(linkedList.containsNodeWithValue(5), True)

