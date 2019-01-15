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
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n==0:
            return 0
        hold = [float('-inf'),-prices[0],-prices[0]]
        notHold = [0]*3
        for i in range(1,n):
            new_hold, new_notHold = [0]*3,[0]*3

            new_notHold[2] = notHold[2]
            new_notHold[1] = max(notHold[1], prices[i]+hold[2])
            new_notHold[0] = max(notHold[0], prices[i]+hold[1])

            new_hold[2] = max(hold[2], notHold[2]-prices[i])
            new_hold[1] = max(hold[1], notHold[1]-prices[i])

            hold, notHold = new_hold, new_notHold
            #print(hold, notHold)
        return max(max(hold),max(notHold))
