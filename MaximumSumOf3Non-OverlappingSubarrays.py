"""
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed).
If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
"""
class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sumToI = [nums[0]]*len(nums)
        # dpleft[i] is starting index and sum of max k subarray sum within range [0,i]
        # dpright[i] is starting index and sum of max k subarray sum within range [i,len(nums)-1]
        dpleft, dpright = [[-1,-1] for _ in range(len(nums))], [[-1,-1] for _ in range(len(nums))]

        # calculate sumToI
        for i in range(1,len(nums)):
            sumToI[i] = sumToI[i-1]+nums[i]

        # calculate dpleft
        maxTotal = sumToI[k-1]
        for i in range(k-1,len(nums)):
            if i==k-1:
                dpleft[i] = [0,maxTotal]
            else:
                total = sumToI[i]-sumToI[i-k]
                if total>maxTotal:
                    maxTotal = total
                    dpleft[i] = [i-k+1,maxTotal]
                else:
                    dpleft[i] = dpleft[i-1]

        # calculate dpright
        maxTotal = sumToI[-1]-sumToI[-k-1]
        for i in range(len(nums)-k,-1,-1):
            if i==len(nums)-k:
                dpright[i] = [len(nums)-k,maxTotal]
            else:
                if i:
                    total = sumToI[i+k-1]-sumToI[i-1]
                else:
                    total = sumToI[k-1]
                if total>=maxTotal:
                    maxTotal = total
                    dpright[i] = [i,maxTotal]
                else:
                    dpright[i] = dpright[i+1]

        # for every possible mid k, calculate final answer
        ret = [0]*3
        maxTotal = -1
        for i in range(k,len(nums)-k):
            if maxTotal==-1:
                maxTotal = dpleft[i-1][1]+sumToI[i+k-1]-sumToI[i-1]+dpright[i+k][1]
                ret = [dpleft[i-1][0], i, dpright[i+k][0]]
            else:
                total = dpleft[i-1][1]+sumToI[i+k-1]-sumToI[i-1]+dpright[i+k][1]
                if total>maxTotal:
                    maxTotal = total
                    ret = [dpleft[i-1][0], i, dpright[i+k][0]]
        return ret
