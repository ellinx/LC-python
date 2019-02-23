"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1


"""
class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        ret = 0
        if not len(intervals):
            return 0
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        total = 0
        i1, i2 = 0, 0
        while i1<len(starts):
            if starts[i1]==ends[i2]:
                i1 += 1
                i2 += 1
                continue
            if starts[i1]<ends[i2]:
                total += 1
                ret = max(ret,total)
                i1 += 1
            else:
                total -= 1
                i2 += 1
        return ret
