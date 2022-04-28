"""
hard

Write a function that takes in three strings and returns a boolean representing whether the
third string can be formed by interweaving the first two strings.

To interweave strings means to merge them by alternating their letters without any specific pattern.
For instance, the strings "abc" and "123" can be interwoven as "a1b2c3", as "abc123", and
as "ab1c23" (this list is nonexhaustive).

Letters within a string must maintain their relative ordering in the interwoven string.

Sample Input
one = "interweave"
two = "this-string"
three = "this-interstringweave"
Sample Output
true
"""
import unittest


def interweavingStrings(one, two, three):
    one_index = 0
    two_index = 0
    for i, char in enumerate(three):
        if one_index < len(one):
            one_char = one[one_index]
        else:
            one_char = ""
        if two_index < len(two):
            two_char = two[two_index]
        else:
            two_char = ""
        if char != one_char and char != two_char:
            return False
        elif char == one_char and char == two_char:
            attempt1 = interweavingStrings(one[one_index:], two[two_index + 1:], three[i + 1:])
            attempt2 = interweavingStrings(one[one_index + 1:], two[two_index:], three[i + 1:])
            return attempt1 or attempt2
        elif char == one_char:
            one_index += 1
        elif char == two_char:
            two_index += 1
    return one_index == len(one) and two_index == len(two)



class TestProgram(unittest.TestCase):
    def test_1(self):
        one = "interweave"
        two = "this-string"
        three = "this-interstringweave"
        self.assertEqual(interweavingStrings(one, two, three), True)

    def test_2(self):
        one = "aabcc"
        two = "dbbca"
        three = "aadbbcbcac"
        self.assertEqual(interweavingStrings(one, two, three), True)

    def test_3(self):
        one = "interweave"
        two = "this-string"
        three = "8this-interstringweave"
        self.assertEqual(interweavingStrings(one, two, three), False)

    def test_4(self):
        one = "interweave"
        two = "this-string"
        three = "this-inter-stringweave"
        self.assertEqual(interweavingStrings(one, two, three), False)
