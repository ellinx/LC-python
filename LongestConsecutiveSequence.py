"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        numsSet = set(nums)
        while len(numsSet):
            for num in numsSet:
                break
            left = 0
            right = 0
            cur = num-1
            while cur in numsSet:
                left += 1
                cur = cur-1
            cur = num+1
            while cur in numsSet:
                right += 1
                cur = cur+1
            ret = max(ret, left+1+right)
            for i in range(num-left,num+right+1):
                numsSet.remove(i)
        return ret
