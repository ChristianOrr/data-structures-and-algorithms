import pytest

from dynamic_programming.levenshtein_distance import (
    levenshtein_distance_1,
)


implementations = [levenshtein_distance_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_levenshtein_basic(fn):
    assert fn("abc", "yabd") == 2


@pytest.mark.parametrize("fn", implementations)
def test_levenshtein_another(fn):
    assert fn("biting", "mitten") == 4
