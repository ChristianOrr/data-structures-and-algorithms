"""
medium

Write a MinMaxStack class for a Min Max Stack. The class should support:

Pushing and popping values on and off the stack.
Peeking at the value at the top of the stack.
Getting both the minimum and the maximum values in the stack at any given point in time.
All class methods, when considered independently, should run in constant time and with constant space.

Sample Usage
// All operations below are performed sequentially.
MinMaxStack(): - // instantiate a MinMaxStack
push(5): -
getMin(): 5
getMax(): 5
peek(): 5
push(7): -
getMin(): 5
getMax(): 7
peek(): 7
push(2): -
getMin(): 2
getMax(): 7
peek(): 2
pop(): 2
pop(): 7
getMin(): 5
getMax(): 5
peek(): 5
"""
import unittest


class MinMaxStack:
    def __init__(self):
        self.array = []
        self.min = None
        self.max = None

    def peek(self):
        return self.array[-1]

    def pop(self):
        removed_value = self.array.pop(-1)
        if self.min == removed_value:
            if len(self.array) != 0:
                self.min = min(self.array)
            else:
                self.min = None

        if self.max == removed_value:
            if len(self.array) != 0:
                self.max = max(self.array)
            else:
                self.max = None
        return removed_value

    def push(self, number):
        self.array.append(number)
        if self.min is None:
            self.min = number
        elif number < self.min:
            self.min = number

        if self.max is None:
            self.max = number
        elif number > self.max:
            self.max = number

    def getMin(self):
        return self.min

    def getMax(self):
        return self.max


def testMinMaxPeek(self, min, max, peek, stack):
    self.assertEqual(stack.getMin(), min)
    self.assertEqual(stack.getMax(), max)
    self.assertEqual(stack.peek(), peek)


class TestProgram(unittest.TestCase):
    def test_1(self):
        stack = MinMaxStack()
        stack.push(5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        stack.push(7)
        testMinMaxPeek(self, 5, 7, 7, stack)
        stack.push(2)
        testMinMaxPeek(self, 2, 7, 2, stack)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 7)
        testMinMaxPeek(self, 5, 5, 5, stack)
        self.assertEqual(stack.pop(), 5)


