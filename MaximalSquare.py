"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4


"""
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not len(matrix):
            return 0
        if not len(matrix[0]):
            return 0
        dp = [[0]*len(matrix[0]) for _ in matrix]
        ret = 0
        # first row
        for i in range(len(matrix[0])):
            if matrix[0][i]=="1":
                dp[0][i] = 1
                ret = 1
        # first col
        for i in range(1, len(matrix)):
            if matrix[i][0]=="1":
                dp[i][0] = 1
                ret = 1
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]=="1":
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
                    ret = max(ret, dp[i][j])
        return ret**2
