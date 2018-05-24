"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class ThreeSum:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # n^2 search
        nums.sort()
        ret = []
        for i in range(len(nums)-2):
            if i and nums[i-1]==nums[i]:
                continue
            target = 0-nums[i]
            left, right = i+1, len(nums)-1
            while left<right:
                if nums[left]+nums[right]>target:
                    right -= 1
                elif nums[left]+nums[right]<target:
                    left += 1
                else:
                    ret.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left += 1
                    while right<left and nums[right]==nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ret
