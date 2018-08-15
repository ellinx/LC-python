"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i1, i2 = 0, 0
        while i2<len(nums):
            if nums[i2]!=0:
                nums[i1] = nums[i2]
                i1 += 1
            i2 += 1
        while i1<len(nums):
            nums[i1] = 0
            i1 += 1
