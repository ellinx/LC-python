"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
"""
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        while idx<len(nums):
            if nums[idx] == idx or nums[idx]>=len(nums):
                idx += 1
                continue
            tmp = nums[idx]
            nums[idx], nums[tmp] = nums[tmp], tmp
        idx = 0
        while idx<len(nums):
            if nums[idx] != idx:
                return idx
            idx += 1
        return idx
