"""
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = [-1,-1]
        # find left bound
        s, e = 0, len(nums)-1
        while s<=e:
            m = s+(e-s)//2
            if nums[m]==target:
                if m-1>=0 and nums[m-1]==target:
                    e = m-1
                    continue
                else:
                    s = m
                    break
            if nums[m]<target:
                s = m+1
            else:
                e = m-1
        if s==len(nums) or nums[s]!=target:
            return ret
        ret[0] = s
        # find right bound
        s, e = 0, len(nums)-1
        while s<=e:
            m = s+(e-s)//2
            if nums[m]==target:
                if m+1<len(nums) and nums[m+1]==target:
                    s = m+1
                    continue
                else:
                    s = m
                    break
            if nums[m]<target:
                s = m+1
            else:
                e = m-1
        ret[1] = s
        return ret
