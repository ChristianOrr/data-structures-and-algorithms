"""
medium

Imagine you have a set of cities that are laid out in a circle, connected by a circular road that runs clockwise.
Each city has a gas station that provides gallons of fuel, and each city is some distance away from the next city.

You have a car that can drive some number of miles per gallon of fuel, and
your goal is to pick a starting city such that you can fill up your car with that city's fuel,
drive to the next city, refill up your car with that city's fuel, drive to the next city, and
so on and so forth until you return back to the starting city with 0 or more gallons of fuel left.

This city is called a valid starting city, and
it's guaranteed that there will always be exactly one valid starting city.

For the actual problem, you'll be given an array of distances such that city i is distances[i] away from city i + 1.
Since the cities are connected via a circular road, the last city is connected to the first city.
In other words, the last distance in the distances array is equal to the distance from the last city to the first city.
You'll also be given an array of fuel available at each city, where fuel[i] is equal to the fuel available at city i.
The total amount of fuel available (from all cities combined) is exactly enough to travel to all cities.
Your fuel tank always starts out empty, and you're given a positive integer value for the
number of miles that your car can travel per gallon of fuel (miles per gallon, or MPG).
You can assume that you will always be given at least two cities.

Write a function that returns the index of the valid starting city.

Sample Input
distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10
Sample Output
4
"""
import unittest
from itertools import accumulate


def validStartingCity(distances, fuel, mpg):
    miles_left = 0
    min_miles_left = 0
    start_city_index = 0

    for i in range(1, len(distances)):
        miles_left += fuel[i - 1] * mpg - distances[i - 1]

        if miles_left < min_miles_left:
            start_city_index = i
            min_miles_left = miles_left

    return start_city_index




class TestProgram(unittest.TestCase):
    def test_1(self):
        distances = [5, 25, 15, 10, 15]
        fuel = [1, 2, 1, 0, 3]
        mpg = 10
        expected = 4
        actual = validStartingCity(distances, fuel, mpg)
        self.assertEqual(actual, expected)

    def test_2(self):
        distances = [5, 20, 20, 10, 15]
        fuel = [1, 0, 3, 0, 3]
        mpg = 10
        expected = 2
        actual = validStartingCity(distances, fuel, mpg)
        self.assertEqual(actual, expected)

    def test_3(self):
        distances = [5, 2, 3]
        fuel = [1, 0, 1]
        mpg = 5
        expected = 2
        actual = validStartingCity(distances, fuel, mpg)
        self.assertEqual(actual, expected)

    def test_4(self):
        distances = [1, 3, 10, 6, 7, 7, 2, 4]
        fuel = [1, 1, 1, 1, 1, 1, 1, 1]
        mpg = 5
        expected = 6
        actual = validStartingCity(distances, fuel, mpg)
        self.assertEqual(actual, expected)

    def test_5(self):
        distances = [30, 40, 10, 10, 17, 13, 50, 30, 10, 40]
        fuel = [1, 2, 0, 1, 1, 0, 3, 1, 0, 1]
        mpg = 25
        expected = 1
        actual = validStartingCity(distances, fuel, mpg)
        self.assertEqual(actual, expected)
