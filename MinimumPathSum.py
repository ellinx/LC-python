"""
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(n):
            if i==0:
                dp[0][0] = grid[0][0]
                continue
            dp[0][i] = dp[0][i-1]+grid[0][i]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        return dp[-1][-1]
