"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []
        if len(intervals) == 0:
            return ret
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0]>cur[1]:
                ret.append(cur)
                cur = intervals[i]
                continue
            cur[1] = max(cur[1], intervals[i][1])
        ret.append(cur)
        return ret
