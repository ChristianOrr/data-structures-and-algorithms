"""
hard

You're given a two-dimensional array (a matrix) of potentially unequal height and width containing letters;
this matrix represents a boggle board. You're also given a list of words.

Write a function that returns an array of all the words contained in the boggle board.
The final words don't need to be in any particular order.

A word is constructed in the boggle board by connecting adjacent (horizontally, vertically,
or diagonally) letters, without using any single letter at a given position more than once;
while a word can of course have repeated letters,
those repeated letters must come from different positions in the boggle board in order for the word to be
contained in the board.
Note that two or more words are allowed to overlap and use the same letters in the boggle board.

Sample Input
board = [
  ["t", "h", "i", "s", "i", "s", "a"],
  ["s", "i", "m", "p", "l", "e", "x"],
  ["b", "x", "x", "x", "x", "e", "b"],
  ["x", "o", "g", "g", "l", "x", "o"],
  ["x", "x", "x", "D", "T", "r", "a"],
  ["R", "E", "P", "E", "A", "d", "x"],
  ["x", "x", "x", "x", "x", "x", "x"],
  ["N", "O", "T", "R", "E", "-", "P"],
  ["x", "x", "D", "E", "T", "A", "E"],
],
words = [
  "this", "is", "not", "a", "simple", "boggle",
  "board", "test", "REPEATED", "NOTRE-PEATED",
]
Sample Output
["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]
// The words could be ordered differently.
"""

def boggle_board_1(board, words):
    first_letters = [word[0] for word in words]
    words_found = []
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if char in first_letters:
                matched_indexes = [i for i, letter in enumerate(first_letters) if letter == char]
                matches_found = []
                words_to_remove = []
                for index in matched_indexes:
                    visited = set()
                    found_word = dfs(i, j, board, words[index], 1, visited)
                    matches_found.append(found_word)
                    if found_word:
                        words_found.append(words[index])
                        words_to_remove.append(words[index])

                # remove the found words, so it doesn't keep searching for it (not essential, but helps efficiency)
                words = [word for word in words if word not in words_to_remove]
                first_letters = [word[0] for word in words if word not in words_to_remove]

    return words_found


def dfs(i, j, board, word, word_index, visited):
    if len(word) < 2:
        return True
    visited.add((i, j))
    next_char = word[word_index]
    neighbours = get_neighbours(i, j, board, visited)
    neighbour_chars = [board[k][l] for (k, l) in neighbours]
    word_index += 1
    for neighbour_index, neighbour_char in enumerate(neighbour_chars):
        if next_char == neighbour_char:
            if word_index == len(word):
                return True
            else:
                (k, l) = neighbours[neighbour_index]
                found_word = dfs(k, l, board, word, word_index, visited)
                if found_word:
                    return True

    visited.remove((i, j))
    return False


def get_neighbours(i, j, board, visited):
    neighbours = [(i - 1, j), (i - 1, j - 1), (i, j - 1), (i + 1, j - 1),
                  (i + 1, j), (i + 1, j + 1), (i, j + 1), (i - 1, j + 1)]

    for neighbour in neighbours.copy():
        if neighbour[0] < 0 or neighbour[1] < 0 or neighbour[0] >= len(board) or neighbour[1] >= len(board[0]):
            neighbours.remove(neighbour)
        elif neighbour in visited:
            neighbours.remove(neighbour)

    return neighbours
