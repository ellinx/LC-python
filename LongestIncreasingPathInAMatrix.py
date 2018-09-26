"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].


Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(matrix, i, j, dp):
            if dp[i][j]!=0:
                return dp[i][j]
            m, n = len(matrix), len(matrix[0])
            dirs = [[-1,0],[1,0],[0,-1],[0,1]]
            ret = 1
            for each in dirs:
                ni = i+each[0]
                nj = j+each[1]
                if ni>=0 and ni<m and nj>=0 and nj<n and matrix[i][j]<matrix[ni][nj]:
                    ret = max(ret, dfs(matrix, ni, nj, dp)+1)
            dp[i][j] = ret
            return ret

        ret = 0
        m = len(matrix)
        if m==0:
            return 0
        n = len(matrix[0])
        # dp[i][j] is longest path starting from matrix[i][j]
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ret = max(ret, dfs(matrix, i, j, dp))
        return ret
