"""
easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.


Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false


Solution 1
Time complexity: O(nlog(n)), Space complexity: O(1)
Strategy:
Sort both strings and return True if they are equal.

Solution 2
Time complexity: O(n), Space complexity: O(n)
Strategy:
Create hash map's to keep count of the number of times a character occurs.
If the hash maps are different, then return False, otherwise return True.
"""
# Solution 1
def is_anagram_1(s, t):
    return sorted(s) == sorted(t)


# Solution 2
def is_anagram_2(s, t):
    if len(s) != len(t):
        return False
    hash_s = {}
    hash_t = {}

    for i in range(len(s)):
        hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
        hash_t[t[i]] = 1 + hash_t.get(t[i], 0)

    for element_s in hash_s.keys():
        if hash_s[element_s] != hash_t.get(element_s, 0):
            return False

    return True

