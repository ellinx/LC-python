"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution:
    # iterative
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cur = [[]]
        for num in nums:
            nxt = []
            for each in cur:
                nxt.append(each+[num])
            cur.extend(nxt)
        return cur

class Solution2:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, start, cur, ret):
            if start==len(nums):
                ret.append(cur)
                return
            dfs(nums, start+1, cur, ret)
            dfs(nums, start+1, cur+[nums[start]], ret)

        ret = []
        dfs(nums, 0, [], ret)
        return ret
