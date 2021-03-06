"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start<=end:
            mid = start+(end-start)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[start]:
                if nums[mid]<target:
                    start = mid+1
                else:
                    if nums[start]>target:
                        start = mid+1
                    else:
                        end = mid-1
            else:
                if nums[mid]<target:
                    if nums[end]<target:
                        end = mid-1
                    else:
                        start = mid+1
                else:
                    end = mid-1
        return -1


class Solution2:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def bSearch(nums, target, l, r):
            while l<=r:
                m = l+(r-l)//2
                if nums[m]==target:
                    return m
                if nums[m]<target:
                    l = m+1
                else:
                    r = m-1
            return -1

        if len(nums)==0:
            return -1
        l, r = 0, len(nums)-1
        while l<r:
            m = l+(r-l)//2
            if nums[m]>nums[r]:
                l = m+1
            else:
                r = m
        idx = l
        #print(idx)
        if target>nums[-1]:
            return bSearch(nums, target, 0, idx)
        return bSearch(nums, target, idx, len(nums))
