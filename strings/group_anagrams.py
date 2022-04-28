"""
medium

Write a function that takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't matter.
For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.

Your function should return a list of anagram groups in no particular order.

Sample Input
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
Sample Output
[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
"""


def groupAnagrams(words):
    grouped_anagrams = {}
    words_sorted = ["".join(sorted(word)) for word in words]
    for i in range(len(words_sorted)):
        if words_sorted[i] not in grouped_anagrams.keys():
            grouped_anagrams[words_sorted[i]] = [words[i]]
        else:
            grouped_anagrams[words_sorted[i]].append(words[i])
    return list(grouped_anagrams.values())


if __name__ == "__main__":
    test = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    out = groupAnagrams(test)
    print(f"The result is : {out}")
