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
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, cur, ret):
            if len(nums)==0:
                ret.append(cur)
                return
            for i,each in enumerate(nums):
                dfs(nums[:i]+nums[i+1:], cur+[each], ret)

        ret = []
        dfs(nums, [], ret)
        return ret
