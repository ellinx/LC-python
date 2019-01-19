"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:
Input: [3,2,3]
Output: [3]

Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return []
        cand1, cnt1 = 0, 0
        cand2, cnt2 = 1, 0
        for num in nums:
            if cand1==num:
                cnt1 += 1
            elif cand2==num:
                cnt2 += 1
            elif cnt1==0:
                cand1, cnt1 = num, 1
            elif cnt2==0:
                cand2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        ret = []
        if nums.count(cand1)>len(nums)/3:
            ret.append(cand1)
        if nums.count(cand2)>len(nums)/3:
            ret.append(cand2)
        return ret
