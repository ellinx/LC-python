"""
Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used
and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(nums, k, start, cur, n, ret):
            if k==0:
                if cur[1]==n:
                    ret.append(cur[0])
                return
            for i in range(start, len(nums)-k+1):
                if cur[1]+nums[i]>n:
                    break
                dfs(nums, k-1, i+1, [cur[0]+[nums[i]], cur[1]+nums[i]], n, ret)

        ret = []
        if k<0 or n<0:
            return []
        dfs([1,2,3,4,5,6,7,8,9], k, 0, [[], 0], n, ret)
        return ret
