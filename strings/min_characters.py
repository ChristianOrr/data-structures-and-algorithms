"""
medium

Write a function that takes in an array of words and returns the smallest array of
characters needed to form all of the words.
The characters don't need to be in any particular order.

For example, the characters ["y", "r", "o", "u"] are needed to form the words ["your", "you", "or", "yo"].

Note: the input words won't contain any spaces; however, they might contain punctuation and/or special characters.

Sample Input
words = ["this", "that", "did", "deed", "them!", "a"]
Sample Output
["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
// The characters could be ordered differently.
"""


def minimum_characters_for_words_1(words):
    chars = []

    for word in words:
        temp_chars = chars.copy()
        for char in word:
            if char not in temp_chars:
                chars.append(char)
            else:
                temp_chars.remove(char)

    return chars
