"""
medium

Write a function that takes in a string of words separated by one or more whitespaces and
returns a string that has these words in reverse order.
For example, given the string "tim is great", your function should return "great is tim".

For this problem, a word can contain special characters, punctuation, and numbers.
The words in the string will be separated by one or more whitespaces, and
the reversed string must contain the same whitespaces as the original string.
For example, given the string "whitespaces    4" you would be expected to return "4    whitespaces".

Note that you're not allowed to use any built-in split or reverse methods/functions.
However, you are allowed to use a built-in join method/function.

Also note that the input string isn't guaranteed to always contain words.

Sample Input
string = "Reverse these words."
Sample Output
"words. these Reverse"
"""
import unittest


def reverseWordsInString(string):
    words = []
    first = 0
    last = 0

    for last, char in enumerate(string):
        if char == " ":
            word = string[first: last]
            words.insert(0, word)
            first = last + 1
            words.insert(0, " ")

    if first <= last:
        word = string[first: last + 1]
        words.insert(0, word)

    return "".join(words)


class TestProgram(unittest.TestCase):
    def test_1(self):
        input = "Reverse these words."
        expected = "words. these Reverse"
        actual = reverseWordsInString(input)
        self.assertEqual(actual, expected)

    def test_2(self):
        input = "bbb  "
        expected = "  bbb"
        actual = reverseWordsInString(input)
        self.assertEqual(actual, expected)

    def test_3(self):
        input = " "
        expected = " "
        actual = reverseWordsInString(input)
        self.assertEqual(actual, expected)
