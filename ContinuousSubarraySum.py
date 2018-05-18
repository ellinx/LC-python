"""
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""

class ContinuousSubarraySum:
    #1 construct sum[i] which stands for the (total sum modular k) from nums[0] to nums[i]
    #2 check if sum[i] exists in sum; if yes then we get an answer
    #3 step 1 and step 2 can be done in one loop
    # note1: sum of nums[i] to nums[j] is sum[j]-sum[i-1]
    # note2: similar to solution of Subarray Sum Equals K
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sum_map = collections.defaultdict(list)
        sum_map[0].append(-1)
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if k:
                total %= k
            li = sum_map[total]
            if len(li) and i-li[0]>1:
                return True
            sum_map[total].append(i)
        return False
