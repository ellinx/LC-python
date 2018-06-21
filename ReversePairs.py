"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2

Example2:

Input: [2,4,3,5,1]
Output: 3

Note:

1. The length of the given array will not exceed 50,000.
2. All the numbers in the input array are in the range of 32-bit integer.

"""
class Solution:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # similar idea of merge sort
        def helper(nums):
            if len(nums)==1:
                return nums
            index = len(nums)//2
            left = helper(nums[:index])
            right = helper(nums[index:])
            # check reverse pairs
            j = 0
            for i in range(len(left)):
                while j<len(right):
                    if left[i]<=2*right[j]:
                        break
                    j += 1
                nonlocal ret
                ret += j
            # merge two sub list
            merged = sorted(left+right)
            return merged

        if len(nums)<2:
            return 0
        ret = 0
        helper(nums)
        return ret
