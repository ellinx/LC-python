"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero),
return the maximum enemies you can kill using one bomb.

The bomb kills all the enemies in the same row and column from the planted point
until it hits the wall since the wall is too strong to be destroyed.

Note: You can only put the bomb at an empty cell.

Example:

Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3
Explanation: For the given grid,

0 E 0 0
E 0 W E
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.
"""
class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])
        row_range = [[0,0] for _ in range(n)]
        ret = 0
        for i in range(m):
            cur_col_range = [0,0]
            for j in range(n):
                if grid[i][j]=='0':
                    total = 0
                    if i>=row_range[j][0]:
                        count = 0
                        # up
                        off = 1
                        while i-off>=0 and grid[i-off][j]!='W':
                            if grid[i-off][j]=='E':
                                count += 1
                            off += 1
                        # down
                        off = 1
                        while i+off<m and grid[i+off][j]!='W':
                            if grid[i+off][j]=='E':
                                count += 1
                            off += 1
                        row_range[j] = [i+off, count]
                    total += row_range[j][1]
                    if j>=cur_col_range[0]:
                        count = 0
                        # left
                        off = 1
                        while j-off>=0 and grid[i][j-off]!='W':
                            if grid[i][j-off]=='E':
                                count += 1
                            off += 1
                        # right
                        off = 1
                        while j+off<n and grid[i][j+off]!='W':
                            if grid[i][j+off]=='E':
                                count += 1
                            off += 1
                        cur_col_range = [j+off,count]
                    total += cur_col_range[1]
                    ret = max(ret, total)
        return ret
