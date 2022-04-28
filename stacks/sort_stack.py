"""
medium

Write a function that takes in an array of integers representing a stack, recursively sorts the stack in place
(i.e., doesn't create a brand new array), and return it.

The array must be treated as a stack, with the end of the array as the top of the stack.
Therefore, you're only allowed to
- Pop elements from the top of the stack by removing elements from
    the end of the array using the built-in .pop() method in your programming language of choice.
- Push elements to the top of the stack by appending elements to the end of the array using the
    built-in .append() method in your programming language of choice.
- Peek at the element on top of the stack by accessing the last element in the array.

You're not allowed to perform any other operations on the input array,
including accessing elements (except for the last element), moving elements, etc..
You're also not allowed to use any other data structures, and your solution must be recursive.

Sample Input
stack = [-5, 2, -2, 4, 3, 1]
Sample Output
[-5, -2, 1, 2, 3, 4]
"""
import unittest


def sortStack(stack):
    return sort(stack)

def sort(stack):
    if len(stack) == 0:
        return stack
    top = stack.pop()
    sort(stack)
    insert(stack, top)
    return stack

def insert(stack, value):
    if len(stack) == 0:
        stack.append(value)
        return
    next_value = stack[-1]
    if next_value <= value:
        stack.append(value)
        return
    else:
        top = stack.pop()
        insert(stack, value)
        stack.append(top)
        return




class TestProgram(unittest.TestCase):
    def test_1(self):
        input = [-5, 2, -2, 4, 3, 1]
        expected = [-5, -2, 1, 2, 3, 4]
        actual = sortStack(input)
        self.assertEqual(actual, expected)

    def test_2(self):
        input = [0, -2, 3, 4, 1, -9, 8]
        expected = [-9, -2, 0, 1, 3, 4, 8]
        actual = sortStack(input)
        self.assertEqual(actual, expected)

    def test_3(self):
        input = [-1, 0, 2, 3, 4, 1, 1, 1]
        expected = [-1, 0, 1, 1, 1, 2, 3, 4]
        actual = sortStack(input)
        self.assertEqual(actual, expected)

