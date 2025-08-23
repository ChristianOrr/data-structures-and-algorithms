"""
medium

Given an array of positive integers representing coin denominations and a single non-negative integer n representing
a target amount of money, write a function that returns the smallest number of coins needed to
make change for (to sum up to) that target amount using the given coin denominations.

Note that you have access to an unlimited amount of coins. In other words,
if the denominations are [1, 5, 10], you have access to an unlimited amount of 1s, 5s, and 10s.

If it's impossible to make change for the target amount, return -1.

Sample Input
n = 7
denoms = [1, 5, 10]
Sample Output
3 // 2x1 + 1x5
"""
def min_number_of_coins_for_change_1(n, denoms):
    min_coins = [float("inf") for i in range(n + 1)]
    min_coins[0] = 0

    for denom in denoms:
        for amount in range(n + 1):
            if denom <= amount:
                coins_required = min_coins[amount - denom] + 1
                min_required = min(min_coins[amount], coins_required)
                min_coins[amount] = min_required

    return min_coins[-1] if min_coins[-1] != float("inf") else -1
