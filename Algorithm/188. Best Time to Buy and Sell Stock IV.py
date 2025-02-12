class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # Initialize DP table
        dp = [[0] * 2 for _ in range(k + 1)]
        for j in range(k + 1):
            dp[j][0] = float('-inf')  # Min cost to buy stock (negative because we need to "spend")

        # DP transition
        for i in range(n):
            for j in range(1, k + 1):  # Transactions indexed from 1 to k
                dp[j][0] = max(dp[j][0], dp[j-1][1] - prices[i])  # Buy at min cost
                dp[j][1] = max(dp[j][1], prices[i] + dp[j][0])    # Sell at max profit

        return dp[k][1]  # Max profit with at most k transactions