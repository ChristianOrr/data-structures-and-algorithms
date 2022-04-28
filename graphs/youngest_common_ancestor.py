"""
medium

You're given three inputs, all of which are instances of an AncestralTree class that
have an ancestor property pointing to their youngest ancestor.
The first input is the top ancestor in an ancestral tree
(i.e., the only instance that has no ancestor--its ancestor property points to None / null), and
the other two inputs are descendants in the ancestral tree.

Write a function that returns the youngest common ancestor to the two descendants.

Note that a descendant is considered its own ancestor.
So in the simple ancestral tree below, the youngest common ancestor to nodes A and B is node A.

// The youngest common ancestor to nodes A and B is node A.
  A
 /
B
Sample Input
// The nodes are from the ancestral tree below.
topAncestor = node A
descendantOne = node E
descendantTwo = node I
          A
       /     \
      B       C
    /   \   /   \
   D     E F     G
 /   \
H     I
Sample Output
node B
"""
import unittest


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depth1 = get_depth(topAncestor, descendantOne)
    depth2 = get_depth(topAncestor, descendantTwo)

    while depth1 != depth2:
        if depth1 < depth2:
            descendantTwo = descendantTwo.ancestor
            depth2 -= 1
        else:
            descendantOne = descendantOne.ancestor
            depth1 -= 1

    while descendantOne.name != descendantTwo.name:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor

    return descendantOne


def get_depth(top, descendant, depth=0):
    if top.name != descendant.name:
        depth += 1
        depth = get_depth(top, descendant.ancestor, depth)
    return depth



class AncestralTree(AncestralTree):
    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self


def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees


class TestProgram(unittest.TestCase):
    def test_1(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"])
        trees["B"].addDescendants(trees["D"], trees["E"])
        trees["D"].addDescendants(trees["H"], trees["I"])
        trees["C"].addDescendants(trees["F"], trees["G"])

        yca = getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"])
        self.assertTrue(yca == trees["B"])
