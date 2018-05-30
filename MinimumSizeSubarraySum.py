"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""
class MinimumSizeSubarraySum:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        total = 0
        start, end = 0, 0
        while end<len(nums):
            while end<len(nums) and total<s:
                total += nums[end]
                end += 1
            if end==len(nums) and total<s:
                break
            if ret==0:
                ret = end-start
            else:
                ret = min(ret,end-start)
            while total>=s:
                ret = min(ret,end-start)
                total -= nums[start]
                start += 1
        return ret
