"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays
where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:

1. 0 < nums.length <= 50000.
2. 0 < nums[i] < 1000.
3. 0 <= k < 10^6.
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ret = 0
        s, e = 0, 0
        cur = 1
        while e<len(nums):
            cur *= nums[e]
            while s<=e and cur>=k:
                cur //= nums[s]
                s += 1
            ret += e-s+1
            e += 1
        return ret
