"""
easy

The Fibonacci sequence is defined as follows: the first number of the sequence is 0,
the second number is 1, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers.
Write a function that takes in an integer n and returns the nth Fibonacci number.

Important note: the Fibonacci sequence is often defined with its first two numbers as F0 = 0 and F1 = 1.
For the purpose of this question, the first Fibonacci number is F0; therefore, getNthFib(1) is equal to F0,
getNthFib(2) is equal to F1, etc..
"""
import unittest


# Solution 1
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    return getNthFib(n - 1) + getNthFib(n - 2)


fib_hash = {1: 0, 2: 1}
# Solution 2
def getNthFib(n):
    if n in fib_hash.keys():
        return fib_hash[n]

    nth = getNthFib(n - 1) + getNthFib(n - 2)
    fib_hash[n] = nth
    return nth


class TestProgram(unittest.TestCase):
    def test_1(self):
        self.assertEqual(getNthFib(6), 5)

    def test_2(self):
        self.assertEqual(getNthFib(15), 377)

    def test_3(self):
        self.assertEqual(getNthFib(11), 55)

    def test_4(self):
        self.assertEqual(getNthFib(18), 1597)

