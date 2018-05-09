"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]
Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: [1, 2, 3, 5]
Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""


class PartitionEqualSubsetSum(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        s = sum(nums)
        if s%2==1:
            return False

        s = s>>1
        dp = [[False]*(s+1) for i in range(n+1)]

        for i in range(n+1):
            dp[i][0] = True

        for i in range(1,n+1):
            for j in range(1,s+1):
                dp[i][j] = dp[i-1][j]
                if nums[i-1]<=j:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]

        return dp[n][s]


if __name__=="__main__":
    tmp = PartitionEqualSubsetSum()
    nums = [1, 5, 2]
    result = tmp.canPartition(nums)
    print(result)
