"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
class BestTimeToBuyAndSellStockIII:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret = 0
        if not len(prices):
            return ret
        # dp[i][j][k] is max profit on day i with max j transactions allowed and hold k share of stock
        dp = [[[0,0] for i in range(3)] for _ in prices]
        dp[0][1][1] = -prices[0]
        dp[0][2][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][1][1]+prices[i])
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][2][1]+prices[i])
            dp[i][1][1] = max(dp[i-1][1][0]-prices[i], dp[i-1][1][1])
            dp[i][2][0] = dp[i-1][2][0]
            dp[i][2][1] = max(dp[i-1][2][0]-prices[i],dp[i-1][2][1])
        return max(max(dp[-1][0]),max(dp[-1][1]),max(dp[-1][2]))
