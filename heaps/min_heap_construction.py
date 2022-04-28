"""
medium

Implement a MinHeap class that supports:

Building a Min Heap from an input array of integers.
Inserting integers in the heap.
Removing the heap's minimum / root value.
Peeking at the heap's minimum / root value.
Sifting integers up and down the heap, which is to be used when inserting and removing values.
Note that the heap should be represented in the form of an array.

Sample Usage
array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]

// All operations below are performed sequentially.
MinHeap(array): - // instantiate a MinHeap (calls the buildHeap method and populates the heap)
buildHeap(array): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
insert(76): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
peek(): -5
remove(): -5 [2, 7, 6, 24, 8, 8, 24, 391, 76, 56, 12, 24, 48, 41]
peek(): 2
remove(): 2 [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48]
peek(): 6
insert(87): - [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48, 87]
"""
import unittest
import math

class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        first_parent = (len(array) - 2) // 2
        for index in reversed(range(first_parent + 1)):
            self.siftDown(index, len(array) - 1, array)
        return array

    def siftDown(self, current_index, end_index, heap):
        left_child = (current_index * 2) + 1
        while left_child <= end_index:
            current_value = heap[current_index]
            right_child = (current_index * 2) + 2 if (current_index * 2) + 2 <= end_index else -1

            left_value = heap[left_child]
            right_value = heap[right_child]

            if right_value != -1 and right_value < left_value and right_value < current_value:
                heap[current_index] = right_value
                heap[right_child] = current_value
                current_index = right_child
            elif left_value < current_value:
                heap[current_index] = left_value
                heap[left_child] = current_value
                current_index = left_child
            else:
                return
            left_child = (current_index * 2) + 1


    def siftUp(self, current_index, heap):

        while current_index != 0:
            parent_index = math.floor((current_index - 1) / 2)
            parent_value = heap[parent_index]
            current_value = heap[current_index]
            if current_value < parent_value:
                heap[current_index] = parent_value
                heap[parent_index] = current_value
                current_index = parent_index
            else:
                return

    def peek(self):
        return self.heap[0]

    def remove(self):
        removed_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)
        self.siftDown(0, len(self.heap) - 1, self.heap)
        self.heap.pop(-1)
        return removed_value


    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        self.siftUp(index, self.heap)



def isMinHeapPropertySatisfied(array):
    for currentIdx in range(1, len(array)):
        parentIdx = (currentIdx - 1) // 2
        if array[parentIdx] > array[currentIdx]:
            return False
    return True


class TestProgram(unittest.TestCase):
    def test_1(self):
        minHeap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
        minHeap.insert(76)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), -5)
        self.assertEqual(minHeap.remove(), -5)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 2)
        self.assertEqual(minHeap.remove(), 2)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 6)
        minHeap.insert(87)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))


    def test_2(self):
        minHeap = MinHeap([2, 3, 1])
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 1)
