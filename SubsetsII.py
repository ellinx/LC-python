"""
Given a collection of integers that might contain duplicates, nums,
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, start, cur, ret):
            ret.append(cur)
            pre = None
            for i in range(start, len(nums)):
                if pre==nums[i]:
                    continue
                dfs(nums, i+1, cur+[nums[i]], ret)
                pre = nums[i]

        nums.sort()
        ret = []
        dfs(nums, 0, [], ret)
        return ret


class Solution2:
    # iterative
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counter = collections.Counter(nums)
        ret = [[]]
        for k in counter:
            nxt = []
            for each in ret:
                for i in range(1,counter[k]+1):
                    nxt.append(each+[k]*i)
            ret.extend(nxt)
        return ret
