"""
Easy

It's photo day at the local school, and you're the photographer assigned to take class photos.
The class that you'll be photographing has an even number of students,
and all these students are wearing red or blue shirts.
In fact, exactly half of the class is wearing red shirts, and the other half is wearing blue shirts.
You're responsible for arranging the students in two rows before taking the photo.
Each row should contain the same number of the students and should adhere to the following guidelines:

All students wearing red shirts must be in the same row.
All students wearing blue shirts must be in the same row.
Each student in the back row must be strictly taller than the student directly in front of them in the front row.
You're given two input arrays: one containing the heights of all the
students with red shirts and another one containing the heights of all the students with blue shirts.
These arrays will always have the same length, and each height will be a positive integer.
Write a function that returns whether or not a class photo that follows the stated guidelines can be taken.

Note: you can assume that each class has at least 2 students.

Sample Input
redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]
Sample Output
true // Place all students with blue shirts in the back row.
"""
import unittest


def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if redShirtHeights[0] > blueShirtHeights[0]:
        back_row = redShirtHeights
        front_row = blueShirtHeights
    else:
        back_row = blueShirtHeights
        front_row = redShirtHeights

    for i in range(len(back_row)):
        back = back_row[i]
        front = front_row[i]

        if front >= back:
            return False

    return True


class TestProgram(unittest.TestCase):
    def test_1(self):
        redShirtHeights = [5, 8, 1, 3, 4]
        blueShirtHeights = [6, 9, 2, 4, 5]
        expected = True
        actual = classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(actual, expected)

    def test_2(self):
        redShirtHeights = [6, 9, 2, 4, 5, 1]
        blueShirtHeights = [5, 8, 1, 3, 4, 9]
        expected = False
        actual = classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(actual, expected)

    def test_3(self):
        redShirtHeights = [5, 4]
        blueShirtHeights = [5, 6]
        expected = True
        actual = classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(actual, expected)
