"""
hard

Write a function that takes in two strings and returns their longest common subsequence.

A subsequence of a string is a set of characters that aren't necessarily adjacent in the string but
that are in the same order as they appear in the string.
For instance, the characters ["a", "c", "d"] form a subsequence of the string "abcd", and
so do the characters ["b", "d"].
Note that a single character in a string and the string itself are both valid subsequences of the string.

You can assume that there will only be one longest common subsequence.

Sample Input
str1 = "ZXVVYZW"
str2 = "XKYKZPW"
Sample Output
["X", "Y", "Z", "W"]
"""
# Solution 
def longest_common_subsequence_1(str1, str2):

    longest_substrings = []

    for r in range(len(str1) + 1):
        row = []
        for c in range(len(str2) + 1):

            if r == 0:
                row = ["" for i in range(len(str2) + 1)]
                break
            elif c == 0:
                row.append("")
            else:
                if str1[r - 1] == str2[c - 1]:
                    substring = longest_substrings[-1][c - 1] + str1[r - 1]
                elif len(longest_substrings[-1][c]) > len(row[-1]):
                    substring = longest_substrings[-1][c]
                else:
                    substring = row[-1]
                row.append(substring)
        longest_substrings.append(row)
    return list(longest_substrings[-1][-1])

