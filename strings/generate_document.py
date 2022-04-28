"""
easy

You're given a string of available characters and a string representing a document that you need to generate.
Write a function that determines if you can generate the document using the available characters.
If you can generate the document, your function should return true; otherwise, it should return false.

You're only able to generate the document if the frequency of unique characters in the
characters string is greater than or equal to the frequency of unique characters in the document string.
For example, if you're given characters = "abcabc" and document = "aabbccc" you cannot
generate the document because you're missing one c.

The document that you need to create may contain any characters,
including special characters, capital letters, numbers, and spaces.

Note: you can always generate the empty string ("").

Sample Input
characters = "atGent!ne reumeDoc"
document = "Generate Document!"
Sample Output
true
"""
import unittest

def find_char(chars, char):
    for j, single_char in enumerate(chars):
        if char == single_char:
            return j
    return -1


def generateDocument(characters, document):
    characters = list(characters)
    if len(characters) < len(document):
        return False

    for i in range(len(document)):
        char = document[i]
        position = find_char(characters, char)
        if position == -1:
            return False
        characters.pop(position)

    return True



class TestProgram(unittest.TestCase):
    def test_1(self):
        characters = "atGent!ne reumeDoc"
        document = "Generate Document!"
        expected = True
        actual = generateDocument(characters, document)
        self.assertEqual(actual, expected)

    def test_2(self):
        characters = "L"
        document = "l"
        expected = False
        actual = generateDocument(characters, document)
        self.assertEqual(actual, expected)

    def test_3(self):
        characters = "l"
        document = "l"
        expected = True
        actual = generateDocument(characters, document)
        self.assertEqual(actual, expected)