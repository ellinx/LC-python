"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

1. Integers in each row are sorted in ascending from left to right.
2. Integers in each column are sorted in ascending from top to bottom.

Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.

"""
class Solution:
    """
    Thoughts:
    1. Start from last element in first row, if target is smaller, go left;
        if target is greater, go down. If it's target, return True
    2. repeat step 1 until out of range.

    Time: O(m+n) where m, n is row and col number of matrix
    Space: O(1)
    """
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m==0:
            return False
        n = len(matrix[0])
        i, j = 0, n-1
        while i<m and j>=0:
            if matrix[i][j]==target:
                return True
            if matrix[i][j]<target:
                i += 1
            else:
                j -= 1
        return False
