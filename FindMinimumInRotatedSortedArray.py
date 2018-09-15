"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:
Input: [3,4,5,1,2]
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0


"""
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, e = 0, len(nums)-1
        while s<e:
            if nums[s]<nums[e]:
                return nums[s]
            m = s+(e-s)//2
            if nums[m]>=nums[s]:
                s = m+1
            else:
                e = m
        return nums[s]
