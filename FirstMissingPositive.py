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
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0:
            return 1
        # first loop put i in nums[i-1]
        idx = 0
        while idx<n:
            if nums[idx]-1<0 or nums[idx]-1>=n or nums[nums[idx]-1]==nums[idx]:
                idx += 1
                continue
            tmp = nums[idx]
            nums[tmp-1], nums[idx] = tmp, nums[tmp-1]
        #print(nums)
        # second loop check unmatched
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1
