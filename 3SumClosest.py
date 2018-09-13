"""
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ret = float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            if nums[i]+nums[l]+nums[l+1]>target:
                if abs(ret-target)>nums[i]+nums[l]+nums[l+1]-target:
                    ret = nums[i]+nums[l]+nums[l+1]
                break
            if nums[i]+nums[r-1]+nums[r]<target:
                if abs(ret-target)>target-(nums[i]+nums[r-1]+nums[r]):
                    ret = nums[i]+nums[r-1]+nums[r]
                continue
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total==target:
                    return target
                if total<target:
                    if abs(ret-target)>target-total:
                        ret = total
                    l += 1
                else:
                    if abs(ret-target)>total-target:
                        ret = total
                    r -= 1
        return ret
