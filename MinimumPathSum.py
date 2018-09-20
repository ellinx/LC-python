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
        if m == 0:
            return 0
        n = len(grid[0])
        cur = [0]*n
        for i in range(n):
            if i==0:
                cur[i] = grid[0][i]
                continue
            cur[i] = cur[i-1]+grid[0][i]
        for i in range(1,m):
            nxt = [0]*n
            for j in range(n):
                if j == 0:
                    nxt[j] = cur[j]+grid[i][j]
                    continue
                nxt[j] = min(cur[j], nxt[j-1])+grid[i][j]
            cur = nxt
        return cur[-1]
