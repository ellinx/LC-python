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
        numSet = set(nums)
        while len(numSet):
            for num in numSet:
                break
            numSet.remove(num)
            l = 1
            while num-l in numSet:
                numSet.remove(num-l)
                l += 1
            r = 1
            while num+r in numSet:
                numSet.remove(num+r)
                r += 1
            ret = max(ret, l+r-1)
        return ret
