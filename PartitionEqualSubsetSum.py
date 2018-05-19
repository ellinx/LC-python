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


class PartitionEqualSubsetSum:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 0/1 knapsack
        total = sum(nums)
        if total%2:
            return False
        total //= 2
        cur = [False]*(total+1)
        cur[0] = True
        if nums[0]<=total:
            cur[nums[0]] = True
        for i in range(1,len(nums)):
            nxt = [False]*(total+1)
            nxt[0] = True
            for j in range(1,total+1):
                # dont take ith
                nxt[j] = cur[j]
                # take ith
                if j>=nums[i]:
                    nxt[j] = nxt[j] or cur[j-nums[i]]
            if nxt[-1]:
                return True
            cur = nxt
        return False


if __name__=="__main__":
    tmp = PartitionEqualSubsetSum()
    nums = [1, 5, 2]
    result = tmp.canPartition(nums)
    print(result)
