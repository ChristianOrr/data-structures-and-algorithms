"""
hard

Write a function that takes in a positive integer numberOfTags and
returns a list of all the valid strings that you can generate with that number of matched <div></div> tags.

A string is valid and contains matched <div></div> tags if for every opening tag <div>,
there's a closing tag </div> that comes after the opening tag and
that isn't used as a closing tag for another opening tag.
Each output string should contain exactly numberOfTags opening tags and numberOfTags closing tags.

For example, given numberOfTags = 2, the valid strings to return would be: ["<div></div><div></div>",
    "<div><div></div></div>"].

Note that the output strings don't need to be in any particular order.

Sample Input
numberOfTags = 3
Sample Output
  [
    "<div><div><div></div></div></div>",
    "<div><div></div><div></div></div>",
    "<div><div></div></div><div></div>",
    "<div></div><div><div></div></div>",
    "<div></div><div></div><div></div>",
  ] // The strings could be ordered differently.
"""
import unittest


def generateDivTags(numberOfTags):
    return add_bracket([], numberOfTags, [])

def add_bracket(bracket_list, num_brackets, bracket_strings):
    if len(bracket_list) == num_brackets * 2:
        bracket_string = "".join(["<div>" if num == 1 else "</div>" for num in bracket_list])
        bracket_strings.append(bracket_string)
        return bracket_strings
    bracket_total = sum(bracket_list)
    brackets_left = num_brackets * 2 - len(bracket_list)

    if bracket_total == 0:
        bracket_list.append(1)
        return add_bracket(bracket_list, num_brackets, bracket_strings)
    elif brackets_left == bracket_total:
        bracket_list.append(-1)
        return add_bracket(bracket_list, num_brackets, bracket_strings)

    bracket_list1 = bracket_list.copy()
    bracket_list1.append(1)
    bracket_strings1 = add_bracket(bracket_list1, num_brackets, bracket_strings)
    bracket_list2 = bracket_list.copy()
    bracket_list2.append(-1)
    bracket_strings2 = add_bracket(bracket_list2, num_brackets, bracket_strings)
    return list(set(bracket_strings1 + bracket_strings2))


class TestProgram(unittest.TestCase):
    def test_1(self):
        input = 3
        expected = [
            "<div><div><div></div></div></div>",
            "<div><div></div><div></div></div>",
            "<div><div></div></div><div></div>",
            "<div></div><div><div></div></div>",
            "<div></div><div></div><div></div>",
        ]
        actual = generateDivTags(input)
        self.assertEqual(actual, expected)


