import pytest

from strings.run_length_encoding import (
    run_length_encoding_1,
)

implementations = [run_length_encoding_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    string = "AAAAAAAAAAAAABBCCCCDD"
    expected = "9A4A2B4C2D"
    actual = fn(string)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    string = "........______=========AAAA   AAABBBB   BBB"
    expected = "8.6_9=4A3 3A4B3 3B"
    actual = fn(string)
    assert actual == expected