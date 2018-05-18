from Interval import Interval
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
class MergeIntervals:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        minHeap = [(intervals[i].start, i, intervals[i]) for i in range(len(intervals))]
        heapq.heapify(minHeap)
        ret = []
        cur = None
        while len(minHeap):
            temp = heapq.heappop(minHeap)[2]
            if not cur:
                cur = temp
                continue
            if temp.start<=cur.end:
                cur.end = max(cur.end, temp.end)
            else:
                ret.append(cur)
                cur = temp
        if cur:
            ret.append(cur)
        return ret
