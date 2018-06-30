"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3


"""
class Solution:
    """
    Thoughts:
    1. for each node "1", DFS mark all its "1" neighbors to "0"

    Time: O((m*n)^2) where m,n is row and col number of grid
    Space: O(1)
    """
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, row, col):
            grid[row][col] = "0"
            dirs = [(-1,0),(1,0),(0,-1),(0,1)]
            for each in dirs:
                i = row+each[0]
                j = col+each[1]
                if i>=0 and i<len(grid) and j>=0 and j<len(grid[0]) and grid[i][j]=="1":
                    dfs(grid, i, j)

        ret = 0
        if len(grid)==0:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    ret += 1
                    dfs(grid, i, j)
        #print(grid)
        return ret
