"""
easy

Create a plot showing cumulative percentage of all times in the array,
[x1, x2, ..., xn] which are greater than a time t0

Example:
X = [0.9, 0.1, 1.5, 3, 0.1, 0, 5, 4]
t0 = 0.5

Graph Axis:
y = [0, 0, 0, 12.5, 25, 37.5, 50, 62.5]
x = [0, 0.1, 0.1, 0.9, 1.5, 3, 4, 5]

Strategy:
Sort the array.
Use the sorted array of times as the x-axis.
Get the percentage for a single element by dividing 1 by the number of elements.
Get the cumulative density function (CDF) by summing the percentage each time the time is greater than the threshold.
Use the CDF and the y-axis, then plot.

"""
import unittest
import matplotlib.pyplot as plt

def create_cdf(x, t0):
    x.sort()
    num_elements = len(x)
    percent_per_element = (1 / num_elements) * 100
    pdf = [percent_per_element if x[i] > t0 else 0 for i in range(num_elements)]
    cdf = [sum(pdf[:i]) for i in range(1, num_elements + 1)]

    return x, cdf

def plot(x, y):

    plt.plot(x, y)
    plt.show()


class TestProgram(unittest.TestCase):
    def test_1(self):
        x = [0.9, 0.1, 1.5, 3, 0.1, 0, 5, 4]
        t0 = 0.5
        pred_x, pred_y = create_cdf(x, t0)
        self.assertEqual((pred_x, pred_y), ([0, 0.1, 0.1, 0.9, 1.5, 3, 4, 5], [0, 0, 0, 12.5, 25, 37.5, 50, 62.5]))
        plot(pred_x, pred_y)



