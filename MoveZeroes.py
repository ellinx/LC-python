"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class MoveZeroes:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index, nonZero = 0, 0
        while nonZero<len(nums):
            while nonZero<len(nums) and nums[nonZero]==0:
                nonZero += 1
            if nonZero==len(nums):
                break
            nums[index] = nums[nonZero]
            index += 1
            nonZero += 1
        while index<len(nums):
            nums[index] = 0
            index += 1
