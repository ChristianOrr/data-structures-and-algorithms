"""
hard

This problem deals with measuring cups that are missing important measuring labels.
Specifically, a measuring cup only has two measuring lines, a Low (L) line and a High (H) line.
This means that these cups can't precisely measure and
can only guarantee that the substance poured into them will be between the L and H line.
For example, you might have a measuring cup that has a Low line at 400ml and a high line at 435ml.
This means that when you use this measuring cup,
you can only be sure that what you're measuring is between 400ml and 435ml.

You're given a list of measuring cups containing their low and
high lines as well as one low integer and one high integer representing a range for a target measurement.
Write a function that returns a boolean representing whether you can use the cups to accurately measure a
volume in the specified [low, high] range (the range is inclusive).

Note that:

Each measuring cup will be represented by a pair of positive integers [L, H], where 0 <= L <= H.
You'll always be given at least one measuring cup,
and the low and high input parameters will always satisfy the following constraint: 0 <= low <= high.
Once you've measured some liquid,
it will immediately be transferred to a larger bowl that will eventually (possibly) contain the target measurement.
You can't pour the contents of one measuring cup into another cup.
Sample Input
measuringCups = [
  [200, 210],
  [450, 465],
  [800, 850],
]
low = 2100
high = 2300
Sample Output
true
// We use cup [450, 465] to measure four volumes:
// First measurement: Low = 450, High = 465
// Second measurement: Low = 450 + 450 = 900, High = 465 + 465 = 930
// Third measurement: Low = 900 + 450 = 1350, High = 930 + 465 = 1395
// Fourth measurement: Low = 1350 + 450 = 1800, High = 1395 + 465 = 1860

// Then we use cup [200, 210] to measure two volumes:
// Fifth measurement: Low = 1800 + 200 = 2000, High = 1860 + 210 = 2070
// Sixth measurement: Low = 2000 + 200 = 2200, High = 2070 + 210 = 2280

// We've measured a volume in the range [2200, 2280].
// This is within our target range, so we return `true`.

// Note: there are other ways to measure a volume in the target range.
"""
import unittest

# Solution 1 (much slower, runs out of time)
def ambiguousMeasurements(measuringCups, low, high):
    sorted_cups = sorted(measuringCups, reverse=True, key=lambda lst: lst[0])
    cups = []
    for cup in sorted_cups:
        if cup[0] > 0 and cup[1] > 0:
            cups.append(cup)

    spread = high - low
    for cup in sorted_cups:
        if cup[1] - cup[0] <= spread:
            return backtrack(cups, low, high, [0, 0])
    return False

def backtrack(cups, low, high, current):
    valid_measurement = False
    useful_cups = cups.copy()
    for cup in cups:
        new_current = [current[0] + cup[0], current[1] + cup[1]]
        if new_current[0] >= low and new_current[1] <= high:
            return True
        elif new_current[0] < low and new_current[1] < high:
            valid_measurement = backtrack(useful_cups, low, high, new_current)
            if valid_measurement:
                return True
        elif new_current[0] > high or new_current[1] > high:
            useful_cups.remove(cup)
    return valid_measurement


# Solution 2
def ambiguousMeasurements(measuringCups, low, high):
    return backtrack(measuringCups, low, high, set())


def backtrack(cups, low, high, failed_set):
    valid_measurement = False
    if (low, high) in failed_set:
        return False

    if low <= 0 and high <= 0:
        return False

    for cup in cups:
        if low <= cup[0] and cup[1] <= high:
            valid_measurement = True
            break

        new_low = low - cup[0]
        new_high = high - cup[1]
        valid_measurement = backtrack(cups, new_low, new_high, failed_set)
        if valid_measurement:
            break

    failed_set.add((low, high)) if not valid_measurement else None
    return valid_measurement


class TestProgram(unittest.TestCase):
    def test_1(self):
        cups = [[200, 210], [450, 465], [800, 850]]
        low = 2100
        high = 2300
        expected = True
        actual = ambiguousMeasurements(cups, low, high)
        self.assertEqual(actual, expected)

    def test_2(self):
        cups = [[1, 3], [2, 4], [5, 6]]
        low = 100
        high = 120
        expected = True
        actual = ambiguousMeasurements(cups, low, high)
        self.assertEqual(actual, expected)

    def test_3(self):
        cups = [[100, 150], [1000, 2000]]
        low = 0
        high = 1000
        expected = True
        actual = ambiguousMeasurements(cups, low, high)
        self.assertEqual(actual, expected)

    def test_4(self):
        cups = [[15, 22]]
        low = 10
        high = 20
        expected = False
        actual = ambiguousMeasurements(cups, low, high)
        self.assertEqual(actual, expected)

    def test_5(self):
        cups = [[50, 65]]
        low = 200
        high = 200
        expected = False
        actual = ambiguousMeasurements(cups, low, high)
        self.assertEqual(actual, expected)