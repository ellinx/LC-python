"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, cur, ret):
            if len(nums)==1:
                ret.append(cur+[nums[0]])
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], cur+[nums[i]], ret)

        ret = []
        if len(nums)==0:
            return ret
        dfs(nums, [], ret)
        return ret
