"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.

"""
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin>=0 and dp[i-coin]!=-1:
                    dp[i] = dp[i-coin]+1 if dp[i]==-1 else min(dp[i], dp[i-coin]+1)
        return dp[amount]
