"""
Given a collection of intervals, find the minimum number of intervals you need to remove
to make the rest of the intervals non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

Example 1:
Input: [ [1,2], [2,3], [3,4], [1,3] ]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:
Input: [ [1,2], [1,2], [1,2] ]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:
Input: [ [1,2], [2,3] ]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Note:
   1. You may assume the interval's end point is always bigger than its start point.
   2. Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

"""
from typing import List

class NonoverlappingIntervals:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        ret = 0
        intervals.sort(key=lambda x:[x[1], -x[0]])
        cur = intervals[0]
        for i in range(1,len(intervals)):
            if cur[1] > intervals[i][0]:
                ret += 1
            else:
                cur = intervals[i]
        return ret


# test
if __name__=="__main__":
    tmp = NonoverlappingIntervals()
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    result = tmp.eraseOverlapIntervals(intervals)
    print(result)
