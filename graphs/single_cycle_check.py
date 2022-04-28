"""
medium

You're given an array of integers where each integer represents a jump of its value in the array.
For instance, the integer 2 represents a jump of two indices forward in the array;
the integer -3 represents a jump of three indices backward in the array.

If a jump spills past the array's bounds, it wraps over to the other side.
For instance, a jump of -1 at index 0 brings us to the last index in the array.
Similarly, a jump of 1 at the last index in the array brings us to index 0.

Write a function that returns a boolean representing whether the jumps in the array form a single cycle.
A single cycle occurs if, starting at any index in the array and following the jumps,
every element in the array is visited exactly once before landing back on the starting index.

Sample Input
array = [2, 3, 1, -4, -4, 2]
Sample Output
true
"""
import unittest

def hasSingleCycle(array):
    if len(array) == 0:
        return True

    for start_index in range(len(array)):
        hash_map = set()
        increment = array[start_index]
        index = start_index

        for _ in range(len(array)):
            index = get_valid_index(index, increment, len(array))
            hash_map.add(index)
            increment = array[index]
        if len(hash_map) == len(array):
            return True
    return False

def get_valid_index(current_index, increment, num_elements):
    new_index = current_index + increment
    if new_index >= num_elements or new_index < 0:
        return new_index % num_elements
    else:
        return new_index



class TestProgram(unittest.TestCase):
    def test_1(self):
        self.assertTrue(hasSingleCycle([2, 3, 1, -4, -4, 2]))

    def test_2(self):
        self.assertTrue(hasSingleCycle([1]))

    def test_3(self):
        self.assertTrue(hasSingleCycle([]))

    def test_4(self):
        self.assertTrue(not hasSingleCycle([3, 1, -1, -3]))

    def test_5(self):
        self.assertTrue(hasSingleCycle([5, 1, 1, -3]))

    def test_6(self):
        self.assertTrue(not hasSingleCycle([0, 1, 1]))