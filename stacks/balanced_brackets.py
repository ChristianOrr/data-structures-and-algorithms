"""
medium

Write a function that takes in a string made up of brackets ((, [, {, ), ], and }) and other optional characters.
The function should return a boolean representing whether the string is balanced with regards to brackets.

A string is said to be balanced if it has as many opening brackets of a certain type as
it has closing brackets of that type and if no bracket is unmatched.
Note that an opening bracket can't match a corresponding closing bracket that comes before it, and
similarly, a closing bracket can't match a corresponding opening bracket that comes after it.
Also, brackets can't overlap each other as in [(]).

Sample Input
string = "([])(){}(())()()"
Sample Output
true // it's balanced
"""
import unittest

class MinMaxStack:
    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[-1]

    def pop(self):
        if len(self.array) > 0:
            removed_bracket = self.array.pop(-1)
        else:
            removed_bracket = ""

        return removed_bracket

    def push(self, bracket):
        self.array.append(bracket)


def balancedBrackets(string):
    brackets = MinMaxStack()
    open = ["{", "[", "("]
    close = ["}", "]", ")"]
    for bracket in string:
        if bracket in open:
            brackets.push(bracket)
        elif bracket in close:
            opening_bracket = brackets.pop()
            bracket_index = close.index(bracket)
            if opening_bracket != open[bracket_index]:
                return False
    if len(brackets.array) == 0:
        return True
    else:
        return False


class TestProgram(unittest.TestCase):
    def test_1(self):
        self.assertEqual(balancedBrackets("([])(){}(())()()"), True)

    def test_2(self):
        self.assertEqual(balancedBrackets(")[]}"), False)

    def test_3(self):
        self.assertEqual(balancedBrackets("()[]{}{"), False)

    def test_4(self):
        self.assertEqual(balancedBrackets("[((([])([]){}){}){}([])[]((())"), False)

    def test_5(self):
        self.assertEqual(balancedBrackets("(z)"), True)