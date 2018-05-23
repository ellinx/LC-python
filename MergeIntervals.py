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
    #1 push all intervals to a min heap
    #2 get the interval of smallest start and merge with current
    #3 if has overlap, merge with current interval; otherwise push current to list and update current
    #4 repeat step 2 until min heap is empty
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
            #very first one
            if not cur:
                cur = temp
                continue

            if temp.start<=cur.end:                 # has overlap, need to merge
                cur.end = max(cur.end, temp.end)
            else:                                   # no overlap, add current and update it
                ret.append(cur)
                cur = temp
        # final one
        if cur:
            ret.append(cur)
        return ret