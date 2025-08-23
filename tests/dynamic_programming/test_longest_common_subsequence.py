import pytest

from dynamic_programming.longest_common_subsequence import (
    longest_common_subsequence_1,
)

implementations = [longest_common_subsequence_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_lcs_basic(fn):
    assert fn("ZXVVYZW", "XKYKZPW") == ["X", "Y", "Z", "W"]


@pytest.mark.parametrize("fn", implementations)
def test_lcs_additional(fn):
    assert fn("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "CCCDDEGDHAGKGLWAJWKJAWGKGWJAKLGGWAFWLFFWAGJWKAG") == ["C", "D", "E", "G", "H", "J", "K", "L", "W"]


@pytest.mark.parametrize("fn", implementations)
def test_lcs_empty(fn):
    assert fn("", "") == []


@pytest.mark.parametrize("fn", implementations)
def test_lcs_one_empty(fn):
    assert fn("", "DJHIO") == []
