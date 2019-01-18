"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = [[0]*n for _ in range(n)]
        num = 1
        start = 0
        while start<=n-1-start:
            if start==n-1-start:
                ret[start][start] = num
                break
            for i in range(start,n-1-start):
                ret[start][i] = num
                num += 1
            for i in range(start,n-1-start):
                ret[i][n-1-start] = num
                num += 1
            for i in range(n-1-start,start,-1):
                ret[n-1-start][i] = num
                num += 1
            for i in range(n-1-start,start,-1):
                ret[i][start] = num
                num += 1
            start += 1
        return ret
