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
class Solution:
    """
    Thoughts:
    1. sort nums
    2. check each triblet start from i(0,len-3)
    3. for rest of triblet use left pointer and right pointer to scan

    Time: O(n^2) where n is length of nums
    Space: O(n)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1]+nums[i+2]>0:
                break
            if nums[i]+nums[-2]+nums[-1]<0:
                continue
            if i>0 and nums[i-1]==nums[i]:
                continue;
            j, k = i+1, len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    ret.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while j<k and nums[j-1]==nums[j]:
                        j += 1
                    k -= 1
                    while k>j and nums[k]==nums[k+1]:
                        k -= 1
                elif nums[i]+nums[j]+nums[k]>0:
                    k -= 1
                else:
                    j += 1
        return ret
