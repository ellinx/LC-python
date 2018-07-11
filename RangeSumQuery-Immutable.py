"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:

1. You may assume that the array does not change.
2. There are many calls to sumRange function.

"""
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sumToIndex = []
        for i in range(len(nums)):
            if i==0:
                self.sumToIndex.append(nums[i])
            else:
                self.sumToIndex.append(self.sumToIndex[i-1]+nums[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i==0:
            return self.sumToIndex[j]
        return self.sumToIndex[j]-self.sumToIndex[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
