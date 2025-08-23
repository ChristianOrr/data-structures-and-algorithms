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

def find_char(chars, char):
    for j, single_char in enumerate(chars):
        if char == single_char:
            return j
    return -1


def generate_document_1(characters, document):
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

