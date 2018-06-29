"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:


"""
class Solution:
    """
    Thoughts:
    1. positions with 4 neighbors have 0 perimeter
    2. positions with 3 neighbors have 1 perimeter
    3. positions with 2 neighbors have 2 perimeter
    4. positions with 1 neighbors have 3 perimeter
    5. positions with 0 neighbors have 4 perimeter

    Time: O(m*n) where m, n is row and col number of the matrix
    Space: O(1)
    """
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    neighbors = 0
                    #up
                    if i-1>=0 and grid[i-1][j]==1:
                        neighbors += 1
                    #down
                    if i+1<m and grid[i+1][j]==1:
                        neighbors += 1
                    #left
                    if j-1>=0 and grid[i][j-1]==1:
                        neighbors += 1
                    #right
                    if j+1<n and grid[i][j+1]==1:
                        neighbors += 1
                    ret += 4-neighbors
        return ret
