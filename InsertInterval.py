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
class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals)==0:
            return [newInterval]
        l, r = 0, len(intervals)-1
        while l<=r:
            m = l+(r-l)//2
            if intervals[m].start==newInterval.start:
                l = m
                break
            if intervals[m].start<newInterval.start:
                l = m+1
            else:
                r = m-1
        if l==0:
            ret = []
            cur = newInterval
        else:
            ret = list(intervals[:l-1])
            cur = intervals[l-1]
            if newInterval.start>cur.end:
                ret.append(cur)
                cur = newInterval
            else:
                cur.end = max(cur.end, newInterval.end)
        for i in range(l,len(intervals)):
            if intervals[i].start>cur.end:
                ret.append(cur)
                cur = intervals[i]
            else:
                cur.end = max(cur.end, intervals[i].end)
        ret.append(cur)
        return ret
