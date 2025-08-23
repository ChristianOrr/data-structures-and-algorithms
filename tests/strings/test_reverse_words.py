import pytest

from strings.reverse_words import (
    reverse_words_in_string_1,
)

implementations = [reverse_words_in_string_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    input = "Reverse these words."
    expected = "words. these Reverse"
    actual = fn(input)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    input = "bbb  "
    expected = "  bbb"
    actual = fn(input)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_3(fn):
    input = " "
    expected = " "
    actual = fn(input)
    assert actual == expected