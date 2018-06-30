"""
 In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0.
 What is the largest axis-aligned plus sign of 1s contained in the grid?
 Return the order of the plus sign.
 If there is none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s.
This is demonstrated in the diagrams below.
Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:

Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000

Example 1:

Input: N = 5, mines = [[4, 2]]
Output: 2
Explanation:
11111
11111
11111
11111
11011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.

Example 2:

Input: N = 2, mines = []
Output: 1
Explanation:
There is no plus sign of order 2, but there is of order 1.

Example 3:

Input: N = 1, mines = [[0, 0]]
Output: 0
Explanation:
There is no plus sign, so return 0.

Note:

    N will be an integer in the range [1, 500].
    mines will have length at most 5000.
    mines[i] will be length 2 and consist of integers in the range [0, N-1].
"""
class Solution:
    """
    Thoughts:
    1. for each node has value 1, check its four directions length and calculate the plus sign order

    Time: O(m*n*(m+n)) where m, n is row and col of matrix
    Space: O(1)
    """
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        grid = [[1]*N for _ in range(N)]
        for each in mines:
            grid[each[0]][each[1]] = 0
        ret = 0
        for i in range(N):
            for j in range(N):
                if ret>=min(i+1,j+1,N-i,N-j):
                    continue
                if grid[i][j]==1:
                    # up
                    offset = 1
                    while i-offset>=0 and grid[i-offset][j]==1:
                        offset += 1
                    order = offset
                    if order<ret:
                        continue
                    # down
                    offset = 1
                    while i+offset<N and grid[i+offset][j]==1:
                        offset += 1
                    order = min(order,offset)
                    if order<ret:
                        continue
                    # left
                    offset = 1
                    while j-offset>=0 and grid[i][j-offset]==1:
                        offset += 1
                    order = min(order,offset)
                    if order<ret:
                        continue
                    # right
                    offset = 1
                    while j+offset<N and grid[i][j+offset]==1:
                        offset += 1
                    order = min(order,offset)
                    ret = max(ret, order)
        return ret
