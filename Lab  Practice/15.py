# knapsack problem

class Solution:
    def knapsack(self, weights, values, capacity):
        n = len(weights)
        dp = [0] * (capacity + 1)

        for i in range(n):
            for w in range(capacity, weights[i] - 1, -1):
                dp[w] = max(
                    dp[w],
                    values[i] + dp[w - weights[i]]
                )

        return dp[capacity]