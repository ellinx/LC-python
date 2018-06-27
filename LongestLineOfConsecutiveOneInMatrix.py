"""
Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.

Example:

Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3

Hint: The number of elements in the given matrix will not exceed 10,000.
"""
class Solution:
    """
    Thoughts:
    1. for each position, check four directions: right, down, right-down, left-down
    2. Update max while checking

    Time: O(mn) where m is total row of matrix and n is total col of matrix
    Space: O(1)
    """
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def check(M,i,j):
            m = len(M)
            n = len(M[0])
            nonlocal ret
            # right
            if j==0 or M[i][j-1]!=1:
                col = j
                while col<n and M[i][col]==1:
                    col += 1
                ret = max(ret, col-j)
            # down
            if i==0 or M[i-1][j]!=1:
                row = i
                while row<m and M[row][j]==1:
                    row += 1
                ret = max(ret, row-i)
            # right down
            if i==0 or j==0 or M[i-1][j-1]!=1:
                row, col = i, j
                while row<m and col<n and M[row][col]==1:
                    row += 1
                    col += 1
                ret = max(ret, row-i)
            # left down
            if i==0 or j==n-1 or M[i-1][j+1]!=1:
                row, col = i, j
                while row<m and col>=0 and M[row][col]==1:
                    row += 1
                    col -= 1
                ret = max(ret, row-i)
            #print(i,j,ret)

        m = len(M)
        if m==0:
            return 0
        n = len(M[0])
        if n==0:
            return 0
        ret = 0
        for i in range(m):
            for j in range(n):
                if M[i][j]==1:
                    check(M,i,j)
        return ret
