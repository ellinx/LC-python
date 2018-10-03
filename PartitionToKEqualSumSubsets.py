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
        def dfs(nums, used, start, total, target, k):
            if total==target:
                if k-1==0:
                    return True
                return dfs(nums, used, 0, 0, target, k-1)
            while start<len(nums) and used[start]:
                start += 1
            pre = None
            for i in range(start,len(nums)):
                if not used[i]:
                    if pre is not None and pre==nums[i]:
                        continue
                    if total+nums[i]>target:
                        break
                    used[i] = True
                    if dfs(nums, used, i+1, total+nums[i], target, k):
                        return True
                    used[i] = False
                    pre = nums[i]
            return False

        if sum(nums)%k != 0:
            return False
        target = sum(nums)//k
        nums.sort()
        if nums[-1]>target:
            return False
        return dfs(nums, [False]*len(nums), 0, 0, target, k)
