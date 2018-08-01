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
        numSet = set(nums)
        ret = 0
        while len(numSet):
            for n in numSet:
                break
            numSet.remove(n)
            l = n-1
            while l in numSet:
                numSet.remove(l)
                l -= 1
            r = n+1
            while r in numSet:
                numSet.remove(r)
                r += 1
            ret = max(ret,r-l-1)
        return ret
