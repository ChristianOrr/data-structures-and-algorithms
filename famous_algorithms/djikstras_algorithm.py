"""
hard

You're given an integer start and a list edges of pairs of integers.

The list is what's called an adjacency list, and it represents a graph.
The number of vertices in the graph is equal to the length of edges,
where each index i in edges contains vertex i's outbound edges, in no particular order.
Each individual edge is represented by an pair of two numbers, [destination, distance],
where the destination is a positive integer denoting the destination vertex and
the distance is a positive integer representing the length of the edge
(the distance from vertex i to vertex destination).
Note that these edges are directed, meaning that you can only travel from a
particular vertex to its destination—not the other way around
(unless the destination vertex itself has an outbound edge to the original vertex).

Write a function that computes the lengths of the shortest paths between start and
all of the other vertices in the graph using Dijkstra's algorithm and returns them in an array.
Each index i in the output array should represent the length of the shortest path between start and vertex i.
If no path is found from start to vertex i, then output[i] should be -1.

Note that the graph represented by edges won't contain any self-loops
(vertices that have an outbound edge to themselves) and
will only have positively weighted edges (i.e., no negative distances).

Sample Input
start = 0
edges = [
  [[1, 7]],
  [[2, 6], [3, 20], [4, 3]],
  [[3, 14]],
  [[4, 2]],
  [],
  [],
]
Sample Output
[0, 7, 13, 27, 10, -1]
"""
import unittest


def dijkstrasAlgorithm(start, edges):
    visited = set()
    shortest_paths = [float("inf") for i in range(len(edges))]
    shortest_paths[start] = 0

    while len(visited) < len(edges):
        shortest = None
        for i in range(len(shortest_paths)):
            if i not in visited:
                if shortest is None:
                    shortest = i
                elif shortest_paths[i] < shortest_paths[shortest]:
                    shortest = i

        for edge in edges[shortest]:
            new_distance = shortest_paths[shortest] + edge[1]
            old_distance = shortest_paths[edge[0]]

            if new_distance < old_distance:
                shortest_paths[edge[0]] = new_distance
        visited.add(shortest)

    result = [-1 if distance == float("inf") else distance for distance in shortest_paths ]
    return result






class TestProgram(unittest.TestCase):
    def test_1(self):
        start = 0
        edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
        expected = [0, 7, 13, 27, 10, -1]
        actual = dijkstrasAlgorithm(start, edges)
        self.assertEqual(actual, expected)

    def test_2(self):
        start = 3
        edges = [[[2, 4]], [[0, 2]], [[1, 1], [3, 2]], [[0, 3]]]
        expected = [3, 8, 7, 0]
        actual = dijkstrasAlgorithm(start, edges)
        self.assertEqual(actual, expected)

    def test_3(self):
        start = 2
        edges = [[], [], [], []]
        expected = [-1, -1, 0, -1]
        actual = dijkstrasAlgorithm(start, edges)
        self.assertEqual(actual, expected)