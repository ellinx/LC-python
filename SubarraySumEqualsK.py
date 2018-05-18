"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

class SubarraySumEqualsK:
    #1 construct sum[i] which stands for the total sum from nums[0] to nums[i]
    #2 check if sum[i]-k exists in sum; if yes then we get an answer
    #3 step 1 and step 2 can be done in one loop
    # note: sum of nums[i] to nums[j] is sum[j]-sum[i-1]
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_map = {}
        sum_map[0] = 1
        total, ret = 0, 0
        for i in range(len(nums)):
            total += nums[i]
            if total-k in sum_map:
                ret += sum_map[total-k]
            if total not in sum_map:
                sum_map[total] = 0
            sum_map[total] += 1
        return ret
