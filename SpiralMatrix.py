"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        m = len(matrix)
        if m==0:
            return ret
        n = len(matrix[0])
        start, end = 0, n-1
        while start<=end and start<=m-1-start:
            for i in range(start,end+1):
                ret.append(matrix[start][i])
            for i in range(start+1,m-start):
                ret.append(matrix[i][end])
            if (start<m-1-start):
                for i in range(end-1,start-1,-1):
                    ret.append(matrix[m-1-start][i])
            if (start<end):
                for i in range(m-2-start,start,-1):
                    ret.append(matrix[i][start])
            #print(start,end,ret)
            start += 1
            end -= 1
        return ret
