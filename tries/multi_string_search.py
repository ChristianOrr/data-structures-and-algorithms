"""
hard

Write a function that takes in a big string and an array of small strings,
all of which are smaller in length than the big string.
The function should return an array of booleans, where each boolean represents whether the
small string at that index in the array of small strings is contained in the big string.

Note that you can't use language-built-in string-matching methods.

Sample Input #1
bigString = "this is a big string"
smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]
Sample Output #1
[true, false, true, true, false, true, false]
Sample Input #2
bigString = "abcdefghijklmnopqrstuvwxyz"
smallStrings = ["abc", "mnopqr", "wyz", "no", "e", "tuuv"]
Sample Output #2
[true, true, false, true, true, false]
"""
import unittest


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):

        for index in range(len(string)):
            trie = self.root
            while index < len(string):
                char = string[index]
                index += 1
                if char not in trie:
                    trie[char] = {}
                trie = trie[char]

            if self.endSymbol not in trie:
                trie[self.endSymbol] = True

    def contains(self, string):
        trie = self.root
        for char in string:
            if char not in trie:
                return False
            trie = trie[char]
        return True


def multiStringSearch(bigString, smallStrings):
    trie = SuffixTrie(bigString)
    result = []
    for small_string in smallStrings:
        result.append(trie.contains(small_string))
    return result




class TestProgram(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            multiStringSearch("this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]),
            [True, False, True, True, False, True, False],
        )

    def test_2(self):
        self.assertEqual(
            multiStringSearch("abcdefghijklmnopqrstuvwxyz", ["abc", "mnopqr", "wyz", "no", "e", "tuuv"]),
            [True, True, False, True, True, False],
        )