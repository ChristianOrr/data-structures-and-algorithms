import pytest

from graphs.youngest_common_ancestor import (
    new_trees,
    get_youngest_common_ancestor_1
)

implementations = [get_youngest_common_ancestor_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    trees = new_trees()
    trees["A"].addDescendants(trees["B"], trees["C"])
    trees["B"].addDescendants(trees["D"], trees["E"])
    trees["D"].addDescendants(trees["H"], trees["I"])
    trees["C"].addDescendants(trees["F"], trees["G"])

    yca = fn(trees["A"], trees["E"], trees["I"])
    assert yca == trees["B"]