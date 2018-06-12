"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        pre = [0]*n
        for i in range(n):
            if obstacleGrid[0][i]==1:
                pre[i] = 0
            else:
                if i==0:
                    pre[i] = 1
                else:
                    pre[i] = pre[i-1]
        for i in range(1,m):
            cur = [0]*n
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    cur[j] = 0
                else:
                    if j==0:
                        cur[j] = pre[j]
                    else:
                        cur[j] = cur[j-1]+pre[j]
            pre = cur
        return pre[-1]
