import pytest

from strings.group_anagrams import (
    group_anagrams_1,
)

implementations = [group_anagrams_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    expected = [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
    output = list(map(lambda x: sorted(x), fn(words)))

    compare(expected, output)

def compare(expected, output):
    if len(expected) == 0:
        assert output == expected
        return
    assert len(expected) == len(output)
    for group in expected:
        assert sorted(group) in output