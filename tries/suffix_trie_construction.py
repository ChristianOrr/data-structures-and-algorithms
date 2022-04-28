"""
medium

Write a SuffixTrie class for a Suffix-Trie-like data structure.
The class should have a root property set to be the root node of the trie and should support:

Creating the trie from a string; this will be done by calling the populateSuffixTrieFrom method upon
class instantiation, which should populate the root of the class.
Searching for strings in the trie.
Note that every string added to the trie should end with the special endSymbol character: "*".

Sample Input (for creation)
string = "babc"
Sample Output (for creation)
The structure below is the root of the trie.
{
  "c": {"*": true},
  "b": {
    "c": {"*": true},
    "a": {"b": {"c": {"*": true}}},
  },
  "a": {"b": {"c": {"*": true}}},
}
Sample Input (for searching in the suffix trie above)
string = "abc"
Sample Output (for searching in the suffix trie above)
true
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
        return True if self.endSymbol in trie else False




class TestProgram(unittest.TestCase):
    def test_1(self):
        trie = SuffixTrie("babc")
        expected = {
            "c": {"*": True},
            "b": {"c": {"*": True}, "a": {"b": {"c": {"*": True}}}},
            "a": {"b": {"c": {"*": True}}},
        }
        self.assertEqual(trie.root, expected)
        self.assertTrue(trie.contains("abc"))