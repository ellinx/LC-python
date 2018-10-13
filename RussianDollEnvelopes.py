"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h).
One envelope can fit into another if and only if both the width and height of one envelope is
greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:
Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""
class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def insertIndex(nums, target):
            s, e = 0, len(nums)-1
            while s<=e:
                m = s+(e-s)//2
                if nums[m]==target:
                    return m
                if nums[m]<target:
                    s = m+1
                else:
                    e = m-1
            return s

        # sort by width, if width is the same, sort by -height
        # check the longest increasing sequence of height in the list
        envelopes.sort(key=lambda x:[x[0],-x[1]])
        heights = []
        for each in envelopes:
            idx = insertIndex(heights, each[1])
            if idx==len(heights):
                heights.append(each[1])
                continue
            heights[idx] = each[1]
        return len(heights)
