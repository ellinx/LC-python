"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""
class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n==0:
            return 0
        if k>=n//2:
            ret = 0
            l, r = 0, 1
            while r<n:
                while r<n and prices[r-1]<=prices[r]:
                    r += 1
                ret += prices[r-1]-prices[l]
                l, r = r, r+1
            return ret
        hold = [-prices[0]]*(k+1)
        notHold = [0]*(k+1)
        for i in range(1,n):
            new_hold, new_notHold = [0]*(k+1), [0]*(k+1)

            for j in range(k,-1,-1):
                if j==k:
                    new_notHold[j] = notHold[j]
                    continue
                new_notHold[j] = max(notHold[j], hold[j+1]+prices[i])

            for j in range(k,-1,-1):
                new_hold[j] = max(hold[j], notHold[j]-prices[i])

            hold, notHold = new_hold, new_notHold
        return max(max(hold),max(notHold))
