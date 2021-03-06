"""
medium

You're given an integer k representing a number of workers and an array of positive integers representing
durations of tasks that must be completed by the workers.
Specifically, each worker must complete two unique tasks and can only work on one task at a time.
The number of tasks will always be equal to 2k such that each worker always has exactly two tasks to complete.
All tasks are independent of one another and can be completed in any order.
Workers will complete their assigned tasks in parallel, and
the time taken to complete all tasks will be equal to the time taken to complete the longest pair of tasks
(see the sample output for an explanation).

Write a function that returns the optimal assignment of
tasks to each worker such that the tasks are completed as fast as possible.
Your function should return a list of pairs,
where each pair stores the indices of the tasks that should be completed by one worker.
The pairs should be in the following format: [task1, task2],
where the order of task1 and task2 doesn't matter.
Your function can return the pairs in any order.
If multiple optimal assignments exist, any correct answer will be accepted.

Note: you'll always be given at least one worker (i.e., k will always be greater than 0).

Sample Input
k = 3
tasks = [1, 3, 5, 3, 1, 4]
Sample Output
{
  {0, 2}, // tasks[0] = 1, tasks[2] = 5 | 1 + 5 = 6
  {4, 5}, // tasks[4] = 1, tasks[5] = 4 | 1 + 4 = 5
  {1, 3}, // tasks[1] = 3, tasks[3] = 3 | 3 + 3 = 6
} // The fastest time to complete all tasks is 6.

// Note: there are multiple correct answers for this sample input.
// The following is an example of another correct answer:
// {
//   {2, 4},
//   {0, 5},
//   {1, 3}
// }
"""
import unittest


def taskAssignment(k, tasks):
    sorted_indexes = sorted(range(len(tasks)), key=lambda i: tasks[i])
    indice_pairs = set()

    while k > 0:
        indice_pairs.add(frozenset([sorted_indexes[k - 1], sorted_indexes[-k]]))
        k -= 1

    return indice_pairs



class TestProgram(unittest.TestCase):
    def test_1(self):
        k = 3
        tasks = [1, 3, 5, 3, 1, 4]
        expected1 = set([frozenset([4, 2]), frozenset([0, 5]), frozenset([3, 1])])
        expected2 = set([frozenset([3, 1]), frozenset([5, 4]), frozenset([2, 0])])
        actual = taskAssignment(k, tasks)
        self.assertTrue(actual == expected1 or actual == expected2)

    def test_2(self):
        k = 1
        tasks = [3, 5]
        expected1 = set([frozenset([0, 1])])
        actual = taskAssignment(k, tasks)
        self.assertTrue(actual == expected1)

    def test_3(self):
        k = 5
        tasks = [3, 7, 5, 4, 4, 3, 6, 8, 3, 3]
        expected1 = set([frozenset([4, 3]), frozenset([2, 9]), frozenset([6, 8]), frozenset([1, 5]), frozenset([7, 0])])
        expected2 = set([frozenset([9, 7]), frozenset([8, 1]), frozenset([5, 6]), frozenset([0, 2]), frozenset([4, 3])])
        actual = taskAssignment(k, tasks)
        self.assertTrue(actual == expected1 or actual == expected2)
