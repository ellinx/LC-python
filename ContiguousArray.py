"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""
class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # treat 1 as 1 and 0 as -1, find longest contiguous subarray with sum 0
        sumIndexes = dict()
        total = 0
        ret = 0
        for i in range(len(nums)):
            if nums[i]==1:
                total += 1
            else:
                total -= 1
            if total==0:
                ret = max(ret, i+1)
                continue
            if total in sumIndexes:
                ret = max(ret, i-sumIndexes[total])
            else:
                sumIndexes[total] = i
        return ret
