"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
class SearchForARange:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = [-1,-1]
        # search lower bound
        start, end = 0, len(nums)-1
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                if mid and nums[mid-1]==target:
                    end = mid-1
                else:
                    ret[0] = mid
                    break
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
        else:
            return ret
        # search upper bound
        start, end = 0, len(nums)-1
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid]==target:
                if mid+1<len(nums) and nums[mid+1]==target:
                    start = mid+1
                else:
                    ret[1] = mid
                    break
            elif nums[mid]>target:
                end = mid-1
            else:
                start = mid+1
        return ret
