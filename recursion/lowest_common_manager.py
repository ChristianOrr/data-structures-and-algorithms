"""
hard

You're given three inputs, all of which are instances of an OrgChart class that have a
directReports property pointing to their direct reports.
The first input is the top manager in an organizational chart
(i.e., the only instance that isn't anybody else's direct report), and
the other two inputs are reports in the organizational chart. The two reports are guaranteed to be distinct.

Write a function that returns the lowest common manager to the two reports.

Sample Input
// From the organizational chart below.
topManager = Node A
reportOne = Node E
reportTwo = Node I
          A
       /     \
      B       C
    /   \   /   \
   D     E F     G
 /   \
H     I
Sample Output
Node B
"""
import unittest


def getLowestCommonManager(topManager, reportOne, reportTwo):
    lcm, _ = find_lcm(topManager, reportOne, reportTwo)
    return lcm

def find_lcm(manager, report1, report2):
    num_important = 0

    for report in manager.directReports:
        lcm, num_important_found = find_lcm(report, report1, report2)
        if lcm is not None:
            return lcm, 2
        num_important += num_important_found

    if manager == report1 or manager == report2:
        num_important += 1

    if num_important == 2:
        return manager, 2
    else:
        return None, num_important


class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

    def addDirectReports(self, directReports):
        for directReport in directReports:
            self.directReports.append(directReport)


ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def getOrgCharts():
    orgCharts = {}
    for letter in ALPHABET:
        orgCharts[letter] = OrgChart(letter)
    return orgCharts


class TestProgram(unittest.TestCase):
    def test_1(self):
        orgCharts = getOrgCharts()
        orgCharts["A"].addDirectReports([orgCharts["B"], orgCharts["C"]])
        orgCharts["B"].addDirectReports([orgCharts["D"], orgCharts["E"]])
        orgCharts["C"].addDirectReports([orgCharts["F"], orgCharts["G"]])
        orgCharts["D"].addDirectReports([orgCharts["H"], orgCharts["I"]])

        lcm = getLowestCommonManager(orgCharts["A"], orgCharts["E"], orgCharts["I"])
        self.assertEqual(lcm.name, "B")
