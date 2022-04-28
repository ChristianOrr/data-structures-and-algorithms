"""
medium

Write a function that takes in two strings and returns the minimum number of edit operations that
need to be performed on the first string to obtain the second string.

There are three edit operations: insertion of a character, deletion of a character,
and substitution of a character for another.

Sample Input
str1 = "abc"
str2 = "yabd"
Sample Output
2 // insert "y"; substitute "c" for "d"
"""
import unittest


def levenshteinDistance(str1, str2):
    min_edits = []
    for i in range(len(str1) + 1):
        row = []
        for j in range(len(str2) + 1):
            if i == 0:
                row = list(range(len(str2) + 1))
                break
            elif j == 0:
                row.append(i)
            else:
                row.append(float("inf"))
        min_edits.append(row)

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            min_prev = min(min_edits[i - 1][j], min_edits[i - 1][j - 1], min_edits[i][j - 1])
            if str1[i - 1] == str2[j - 1]:
                min_edits[i][j] = min_edits[i - 1][j - 1]
            else:
                min_edits[i][j] = min_prev + 1

    return min_edits[-1][-1]



class TestProgram(unittest.TestCase):
    def test_1(self):
        self.assertEqual(levenshteinDistance("abc", "yabd"), 2)

    def test_2(self):
        self.assertEqual(levenshteinDistance("biting", "mitten"), 4)