"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

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
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()
        ret = 0
        cur = 0
        index1, index2 = 0,0
        while index1<len(intervals) and index2<len(intervals):
            if starts[index1]==ends[index2]:
                index1 += 1
                index2 += 1
                continue
            if starts[index1]<ends[index2]:
                cur += 1
                ret = max(ret,cur)
                index1 += 1
            else:
                cur -= 1
                index2 += 1
        return ret
