"""
easy

Write a function that takes in a non-empty string and
that returns a boolean representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward and backward.
Note that single-character strings are palindromes.

Sample Input
string = "abcdcba"
Sample Output
true // it's written the same forward and backward

Solution 1
Time complexity: O(n), Space complexity: O(n)
Strategy:
Reverse the string. If string == reversed_string return True, else False.

Solution 2
Time complexity: O(n), Space complexity: O(1)
Strategy:
Use while loop with double pointer on left and right ends. If left_value != right_value return False else
increment left index and decrement right index and continue.
Return True if the loop completes without finding a miss-match.

"""
import unittest

# Solution 1 O(n)
def isPalindrome(string):

    if string == string[::-1]:
        return True
    return False

# Solution 2 O(n)
def isPalindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        left_value = string[left]
        right_value = string[right]
        if left_value != right_value:
            return False
        left += 1
        right -= 1

    return True



class TestProgram(unittest.TestCase):
    def test_1(self):
        self.assertEqual(isPalindrome("abcdcba"), True)

    def test_2(self):
        self.assertEqual(isPalindrome("m"), True)

    def test_3(self):
        self.assertEqual(isPalindrome("bd"), False)