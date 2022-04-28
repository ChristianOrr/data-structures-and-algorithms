"""
medium

You're given two positive integers representing the height of a staircase and
the maximum number of steps that you can advance up the staircase at a time.
Write a function that returns the number of ways in which you can climb the staircase.

For example, if you were given a staircase of height = 3 and maxSteps = 2 you could climb the staircase in 3 ways.
You could take 1 step, 1 step, then 1 step, you could also take 1 step,
then 2 steps, and you could take 2 steps, then 1 step.

Note that maxSteps <= height will always be true.

Sample Input
height = 4
maxSteps = 2
Sample Output
5
// You can climb the staircase in the following ways:
// 1, 1, 1, 1
// 1, 1, 2
// 1, 2, 1
// 2, 1, 1
// 2, 2
"""
import unittest


def staircaseTraversal(height, maxSteps, current_height=0, num_ways=0):

    for step in range(1, maxSteps + 1):
        new_height = current_height + step
        if new_height == height:
            num_ways += 1
        elif new_height < height:
            num_ways = staircaseTraversal(height, maxSteps, new_height, num_ways)

    return num_ways



class TestProgram(unittest.TestCase):
    def test_1(self):
        stairs = 4
        maxSteps = 2
        expected = 5
        actual = staircaseTraversal(stairs, maxSteps)
        self.assertEqual(actual, expected)

    def test_2(self):
        stairs = 3
        maxSteps = 2
        expected = 3
        actual = staircaseTraversal(stairs, maxSteps)
        self.assertEqual(actual, expected)

    def test_3(self):
        stairs = 15
        maxSteps = 5
        expected = 13624
        actual = staircaseTraversal(stairs, maxSteps)
        self.assertEqual(actual, expected)

    def test_4(self):
        stairs = 4
        maxSteps = 4
        expected = 8
        actual = staircaseTraversal(stairs, maxSteps)
        self.assertEqual(actual, expected)

    def test_5(self):
        stairs = 14
        maxSteps = 1
        expected = 1
        actual = staircaseTraversal(stairs, maxSteps)
        self.assertEqual(actual, expected)