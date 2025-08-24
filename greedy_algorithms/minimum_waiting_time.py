"""
Easy

You're given a non-empty array of positive integers representing the
amounts of time that specific queries take to execute.
Only one query can be executed at a time, but the queries can be executed in any order.

A query's waiting time is defined as the amount of time that it must wait before its execution starts.
In other words, if a query is executed second, then its waiting time is the duration of the first query;
if a query is executed third, then its waiting time is the sum of the durations of the first two queries.

Write a function that returns the minimum amount of total waiting time for all of the queries.
For example, if you're given the queries of durations [1, 4, 5],
then the total waiting time if the queries were executed in the order of [5, 1, 4] would be (0) + (5) + (5 + 1) = 11.
The first query of duration 5 would be executed immediately,
so its waiting time would be 0, the second query of duration 1 would have to wait 5 seconds
(the duration of the first query) to be executed, and
the last query would have to wait the duration of the first two queries before being executed.

Note: you're allowed to mutate the input array.

Sample Input
queries = [3, 2, 1, 2, 6]
Sample Output
17

Solution 1
Time Complexity: O(nlog(n)), space complexity: O(n)
Strategy:
Sort the array, then remove the last element.
Accumulate the array, then sum up the accumulation and return the sum.

Solution 2
Time Complexity: O(nlog(n)), space complexity: O(1)
Strategy:
Sort the array. Keep track of total_waiting_time and num_queries_left.
Iterate over the array and add num_queries_left * current_waiting_time to total_waiting_time.
Return the total_waiting_time after the loop.

"""
# Solution 1
def minimum_waiting_time_1(queries):
    queries.sort()
    queries.pop(-1)

    accum = [sum(queries[:i + 1]) for i in range(len(queries))]

    return sum(accum)


# Solution 2
def minimum_waiting_time_2(queries):
    queries.sort()
    total_waiting_time = 0
    queries_left = len(queries) - 1

    for current_waiting_time in queries:
        total_waiting_time += current_waiting_time * queries_left
        queries_left -= 1

    return total_waiting_time

