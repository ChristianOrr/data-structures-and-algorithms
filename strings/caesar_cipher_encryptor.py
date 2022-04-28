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
"""

def caesarCipherEncryptor(string, key):
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

if __name__ == "__main__":
    test = "xyz"
    key = 2
    out = caesarCipherEncryptor(test, key)
    print(f"The result is : {out}")
