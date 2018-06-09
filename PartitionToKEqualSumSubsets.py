"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Note:
1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""
class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def dfs(nums, used, start, cur, total, target):
            #print(used,total)
            if total==0:
                if cur==0:
                    return True
                return False
            pre = None
            for i in range(start, len(nums)):
                if used[i] or nums[i]==pre:
                    continue
                if cur+nums[i]>target:
                    break
                used[i] = True
                if cur+nums[i]==target:
                    if dfs(nums, used, 0, 0, total-1, target):
                        return True
                else:
                    if dfs(nums, used, i+1, cur+nums[i], total-1, target):
                        return True
                pre = nums[i]
                used[i] = False
            return False

        total = sum(nums)
        if total%k!=0:
            return False
        target = total//k
        if max(nums)>target:
            return False
        used = [False]*len(nums)
        nums.sort()
        return dfs(nums, used, 0, 0, len(nums), target)
