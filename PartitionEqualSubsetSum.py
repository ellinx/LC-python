"""
Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
1. Each of the array element will not exceed 100.
2. The array size will not exceed 200.

Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total%2==1:
            return False
        target = total//2
        # dp[i][j] means if first i numbers in nums can sum to j
        dp = [[False]*(target+1) for _ in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] = True
        for i in range(1, len(nums)+1):
            for j in range(1, target+1):
                # if not take ith number
                dp[i][j] = dp[i-1][j]
                # if take ith number
                if j-nums[i-1]>=0:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]
        return dp[len(nums)][target]


if __name__=="__main__":
    tmp = PartitionEqualSubsetSum()
    nums = [1, 5, 2]
    result = tmp.canPartition(nums)
    print(result)
