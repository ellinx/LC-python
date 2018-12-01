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
        l, r = 0 ,len(intervals)-1
        while l<=r:
            m = l+(r-l)//2
            if intervals[m].start==newInterval.start:
                l = m
                break
            if intervals[m].start<newInterval.start:
                l = m+1
            else:
                r = m-1
        curInterval = Interval()
        ret = []
        if l==0:
            curInterval = newInterval
        else:
            ret.extend(intervals[:l-1])
            if newInterval.start>intervals[l-1].end:
                ret.append(intervals[l-1])
                curInterval = newInterval
            else:
                curInterval.start = intervals[l-1].start
                curInterval.end = max(intervals[l-1].end, newInterval.end)
        for i in range(l,len(intervals)):
            if intervals[i].start>curInterval.end:
                ret.append(curInterval)
                curInterval = intervals[i]
            else:
                curInterval.end = max(intervals[i].end, curInterval.end)
        ret.append(curInterval)
        return ret
