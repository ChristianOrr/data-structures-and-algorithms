"""
medium

Write a function that takes in a non-empty array of integers and returns an array of the same length,
where each element in the output array is equal to the product of every other number in the input array.

In other words, the value at output[i] is equal to the product of every number in the input array other than input[i].

Note that you're expected to solve this problem without using division.

Sample Input
array = [5, 1, 4, 2]
Sample Output
[8, 40, 10, 20]
// 8 is equal to 1 x 4 x 2
// 40 is equal to 5 x 4 x 2
// 10 is equal to 5 x 1 x 2
// 20 is equal to 5 x 1 x 4
"""

# Solution 1 O(n^2)
def array_of_products_solution_1(array):
    output = []
    for i in range(len(array)):
        prod = 1
        for j in range(len(array)):
            if i != j:
                prod *= array[j]

        output.append(prod)

    return output

# Solution 2 O(n)
def array_of_products_solution_2(array):

    prods = [1 for i in range(len(array))]
    right_prods = prods.copy()
    left_prods = prods.copy()
    prod = 1
    for i in range(len(array)):
        left_prods[i] = prod
        prod *= array[i]

    prod = 1
    for i in reversed(range(len(array))):
        right_prods[i] = prod
        prod *= array[i]

    for i in range(len(array)):
        prods[i] = left_prods[i] * right_prods[i]

    return prods
