"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


"""
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] is min and max product ends at i
        dp = [[0,0] for _ in nums]
        dp[0] = [nums[0], nums[0]]
        ret = nums[0]
        for i in range(1,len(nums)):
            if nums[i]==0:
                dp[i] = [0,0]
                continue
            dp[i][0] = min(nums[i], nums[i]*dp[i-1][0], nums[i]*dp[i-1][1])
            dp[i][1] = max(nums[i], nums[i]*dp[i-1][0], nums[i]*dp[i-1][1])
            ret = max(ret, dp[i][1])
        #print(dp)
        return ret
