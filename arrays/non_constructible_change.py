"""
easy

Given an array of positive integers representing the values of coins in your possession,
write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create.
The given coins can have any positive integer value and aren't necessarily unique
(i.e., you can have multiple coins of the same value).

For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4.
If you're given no coins, the minimum amount of change that you can't create is 1.
"""
import unittest


def nonConstructibleChange(coins):
    coins.sort()
    change = 0
    for coin in coins:
        if change + 1 < coin:
            return change + 1
        change += coin
    return change + 1


class TestProgram(unittest.TestCase):
    def test_1(self):
        input = [5, 7, 1, 1, 2, 3, 22]
        expected = 20
        actual = nonConstructibleChange(input)
        self.assertEqual(actual, expected)

    def test_2(self):
        input = []
        expected = 1
        actual = nonConstructibleChange(input)
        self.assertEqual(actual, expected)

    def test_3(self):
        input = [1, 1]
        expected = 3
        actual = nonConstructibleChange(input)
        self.assertEqual(actual, expected)



