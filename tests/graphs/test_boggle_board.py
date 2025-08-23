import pytest

from graphs.boggle_board import (
    boggle_board_1,
)

implementations = [boggle_board_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
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
    ]
    words = ["this", "is", "not", "a", "simple", "boggle", "board", "test", "REPEATED", "NOTRE-PEATED"]
    expected = ["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]
    actual = fn(board, words)
    assert len(actual) == len(expected)
    for word in actual:
        assert word in expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    board = [
        ["a", "b", "c", "d", "e"],
        ["f", "g", "h", "i", "j"],
        ["k", "l", "m", "n", "o"],
        ["p", "q", "r", "s", "t"],
        ["u", "v", "w", "x", "y"]
    ]
    words = ["agmsy", "agmsytojed", "agmsytojedinhcbgl", "agmsytojedinhcbfl"]
    expected = ["agmsy", "agmsytojed", "agmsytojedinhcbfl"]
    actual = fn(board, words)
    assert len(actual) == len(expected)
    for word in actual:
        assert word in expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_3(fn):
    board = [
        ["a", "b"],
        ["c", "d"]
    ]
    words = ["abcd", "abdc", "acbd", "acdb", "adbc", "adcb", "abca"]
    expected = ["abcd", "abdc", "acbd", "acdb", "adbc", "adcb"]
    actual = fn(board, words)
    assert len(actual) == len(expected)
    for word in actual:
        assert word in expected