"""
Given an array of n integers nums and a target,
find the number of index triplets i, j, k with 0 <= i < j < k < n that
satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:
Input: nums = [-2,0,1,3], and target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
             
Follow up: Could you solve it in O(n2) runtime?
"""
class Solution:
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        ret = 0
        for i in range(n-2):
            if nums[i]+nums[i+1]+nums[i+2]>=target:
                break
            if nums[i]+nums[-2]+nums[-1]<target:
                ret += (1+n-i-2)*(n-i-2)//2
                continue
            j, k = i+1, n-1
            while j<k:
                if nums[i]+nums[j]+nums[k]>=target:
                    k -= 1
                else:
                    ret += k-j
                    j += 1
        return ret
