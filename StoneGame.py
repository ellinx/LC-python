"""
Alex and Lee play a game with piles of stones.
There are an even number of piles arranged in a row,
and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.
The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.
Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.
This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.



Example 1:

Input: [5,3,4,5]
Output: true
Explanation:
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.


Note:

1. 2 <= piles.length <= 500
2. piles.length is even.
3. 1 <= piles[i] <= 500
4. sum(piles) is odd.
"""
class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for i in range(1,n):
            r, c = 0, i
            while c<n:
                dp[r][c] = max(piles[r]-dp[r+1][c], piles[c]-dp[r][c-1])
                r, c = r+1, c+1
        #print(dp)
        return dp[0][n-1]>0

class Solution2:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        def dfs(piles, start, end, mm):
            if start>end:
                return 0
            key = str(start)+","+str(end)
            if key in mm:
                return mm[key]
            l = piles[start]-dfs(piles, start+1, end, mm)
            r = piles[end]-dfs(piles, start, end-1, mm)
            mm[key] = max(l,r)
            return mm[key]

        return dfs(piles, 0, len(piles)-1, dict())>0
