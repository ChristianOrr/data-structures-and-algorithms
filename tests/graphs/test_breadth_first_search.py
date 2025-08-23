import pytest

from graphs.breadth_first_search import (
    Node,
)

implementations = [Node]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    graph = fn("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    assert graph.breadthFirstSearch([]) == ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]