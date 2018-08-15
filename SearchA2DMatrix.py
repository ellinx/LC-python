"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

1. Integers in each row are sorted from left to right.
2. The first integer of each row is greater than the last integer of the previous row.

Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false


"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def insertIndex(nums, target):
            start, end = 0, len(nums)-1
            while start<=end:
                mid = start+(end-start)//2
                if nums[mid]==target:
                    return mid
                if nums[mid]>target:
                    end = mid-1
                else:
                    start = mid+1
            return start

        m = len(matrix)
        if m==0:
            return False
        n = len(matrix[0])
        if n==0:
            return False
        row = insertIndex([each[0] for each in matrix],target)
        if row<m and matrix[row][0]==target:
            return True
        if row==0:
            return False
        col = insertIndex(matrix[row-1],target)
        if col==len(matrix[row-1]):
            return False
        return matrix[row-1][col]==target
