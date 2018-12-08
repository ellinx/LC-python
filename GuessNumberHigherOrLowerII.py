"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x.
You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
"""
class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in range(n+1)]
        off = 1
        while off<=n-1:
            i, j = 1, 1+off
            while j<=n:
                dp[i][j] = float('inf')
                for k in range(i,j):
                    dp[i][j] = min(dp[i][j], k+max(dp[i][k-1],dp[k+1][j]))
                i += 1
                j += 1
            off += 1
        return dp[1][n]
