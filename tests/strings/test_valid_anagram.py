import pytest

from strings.valid_anagram import (
    is_anagram_1,
    is_anagram_2
)

implementations = [is_anagram_1, is_anagram_2]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    s = "anagram"
    t = "nagaram"
    assert fn(s, t)

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    s = "anagran"
    t = "nagaram"
    assert not fn(s, t)