"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if intervals[mid][0] == newInterval[0]:
                l = mid
                break
            if intervals[mid][0] < newInterval[0]:
                l = mid + 1
            else:
                r = mid - 1
        if l == 0:
            ret = []
            cur = newInterval
        else:
            if intervals[l-1][1] < newInterval[0]:
                ret = intervals[:l]
                cur = newInterval
            else:
                ret = intervals[:l-1]
                cur = [min(intervals[l-1][0], newInterval[0]), max(intervals[l-1][1], newInterval[1])]
        for i in range(l, len(intervals)):
            if cur[1] < intervals[i][0]:
                ret.append(cur)
                return ret + intervals[i:]
            cur[1] = max(cur[1], intervals[i][1])
        ret.append(cur)
        return ret


if __name__ == "__main__":
    intervals = [[1,3], [6,9]]
    newInterval = [2,5]
    test = Solution()
    print(test.insert(intervals, newInterval))
