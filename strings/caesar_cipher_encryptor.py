"""
easy

Given a non-empty string of lowercase letters and a non-negative integer representing a key,
write a function that returns a new string obtained by shifting every letter in the input string by
k positions in the alphabet, where k is the key.

Note that letters should "wrap" around the alphabet; in other words,
the letter z shifted by one returns the letter a.

Sample Input
string = "xyz"
key = 2
Sample Output
"zab"

Solution 1
Time Complexity: O(n), space complexity: O(n)
Strategy:
Create an alphabet string and convert it to a list. Create an empty new_sting.
Iterate over the letters of the string. Find the letter_index in the alphabet list and increment it by key.
Make sure the letter_index doesn't go out of bounds by using modulo.
Get the new_letter in alphabet using the valid letter_index and add it to the new_string.
After the loop return the new_string.
"""

# Solution 1
def caesar_cipher_encryptor_1(string, key):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    alphabet_length = len(alphabet)
    new_string = ""
    for letter in string:
        letter_index = alphabet.index(letter)
        letter_index += key
        if letter_index >= alphabet_length:
            letter_index = letter_index % alphabet_length
        new_letter = alphabet[letter_index]
        new_string += new_letter
    return new_string


