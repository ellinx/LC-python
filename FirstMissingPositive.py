"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""

class FirstMissingPositive:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # first loop put i in nums[i-1]
        index = 0
        while index<len(nums):
            if nums[index]>0 and nums[index]<=len(nums) and nums[nums[index]-1]!=nums[index]:
                temp = nums[nums[index]-1]
                nums[nums[index]-1] = nums[index]
                nums[index] = temp
            else:
                index += 1
        # second loop check unmatched
        for index in range(len(nums)):
            if nums[index]!=index+1:
                return index+1
        return len(nums)+1
