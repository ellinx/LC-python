"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak
such that i < j < k and ai < ak < aj.
Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]
Output: False
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: [3, 1, 4, 2]
Output: True
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: [-1, 3, 2, 0]
Output: True
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""
class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n<3:
            return False
        mn = [nums[0]]*n
        for i in range(n):
            mn[i] = min(mn[i-1], nums[i])
        stk = collections.deque()
        ak = float('-inf')
        for j in range(n-1,0,-1):
            while len(stk)>0 and nums[j]>=stk[-1]:
                if stk[-1]<nums[j]:
                    ak = stk[-1]
                stk.pop()
            if mn[j-1]<ak:
                return True
            stk.append(nums[j])
        return False
