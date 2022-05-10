"""
easy

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

Solution 1
Time complexity: O(n), Space complexity: O(n)
Strategy:
Create a stack (list) to store all the opening brackets.
Create a hash-map mapping the closing brackets to the correct opening brackets.
When an opening bracket is encountered add it to the stack.
When a closing bracket is found, check if its opening bracket is at the top of the stack.
If it is, then pop it off the stack and continue, else return False.
At the end of the loop if the stack is empty return True, else return False.
"""
import unittest


def balancedBrackets(string):
    stack = []
    bracket_map = {")": "(", "]": "[", "}": "{"}

    for brace in string:
        if brace in bracket_map.keys():
            if len(stack) > 0 and bracket_map[brace] == stack[-1]:
                stack.pop()
            else:
                return False
        elif brace in bracket_map.values():
            stack.append(brace)

    return len(stack) == 0



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