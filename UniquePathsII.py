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
        if m==0:
            return 0
        n = len(obstacleGrid[0])
        cur = [0]*n
        if obstacleGrid[0][0]==1:
            return 0
        cur[0] = 1
        for i in range(1,n):
            if obstacleGrid[0][i]==1:
                cur[i] = 0
                continue
            cur[i] = cur[i-1]
        #print(cur)
        for i in range(1,m):
            nxt = [0]*n
            if obstacleGrid[i][0]==0:
                nxt[0] = cur[0]
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    nxt[j] = 0
                    continue
                nxt[j] = cur[j]+nxt[j-1]
            cur = nxt
            #print(cur)
        return cur[-1]
