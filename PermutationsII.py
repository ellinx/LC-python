"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, used, cur, ret):
            if len(cur)==len(nums):
                ret.append(cur)
                return
            preUsed = set()
            for i in range(len(nums)):
                if used[i]:
                    continue
                if nums[i] not in preUsed:
                    used[i] = True
                    dfs(nums, used, cur+[nums[i]], ret)
                    used[i] = False
                    preUsed.add(nums[i])

        used = [False]*len(nums)
        nums.sort()
        ret = []
        dfs(nums, used, [], ret)
        return ret
