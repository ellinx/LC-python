"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer
which has exactly the same digits existing in the integer n and is greater in value than n.
If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21



Example 2:

Input: 21
Output: -1

"""
class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        ret = [-1]*N
        stk = collections.deque()
        for i in range(2*N):
            idx = i%N
            while len(stk) and nums[stk[-1]]<nums[idx]:
                ret[stk.pop()] = nums[idx]
            if idx<N:
                stk.append(idx)
        return ret
