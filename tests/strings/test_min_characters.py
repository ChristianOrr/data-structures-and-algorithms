import pytest

from strings.min_characters import (
    minimum_characters_for_words_1,
)

implementations = [minimum_characters_for_words_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    input = ["this", "that", "did", "deed", "them!", "a"]
    expected = ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
    actual = fn(input)
    assert sorted(actual) == sorted(expected)

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    input = ["your", "you", "or", "yo"]
    expected = ["y", "r", "o", "u"]
    actual = fn(input)
    assert sorted(actual) == sorted(expected)