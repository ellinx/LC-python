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
class Solution:
    # first loop put i in nums[i-1]
    # second loop check unmatched
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        idx = 0
        while idx<len(nums):
            if nums[idx]==idx+1 or nums[idx]<1 or nums[idx]>len(nums):
                idx += 1
                continue
            if nums[nums[idx]-1]!=nums[idx]:
                temp = nums[nums[idx]-1]
                nums[nums[idx]-1] = nums[idx]
                nums[idx] = temp
            else:
                idx += 1
        #print(nums)
        for i in range(len(nums)):
            if nums[i]==i+1:
                continue
            return i+1
        return len(nums)+1
