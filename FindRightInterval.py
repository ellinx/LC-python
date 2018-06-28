from Interval import *

"""
Given a set of intervals, for each of the interval i,
check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i,
which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index,
which means that the interval j has the minimum start point to build the "right" relationship for interval i.
If the interval j doesn't exist, store -1 for the interval i.
Finally, you need output the stored value of each interval as an array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.

Example 1:
Input: [ [1,2] ]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:
Input: [ [3,4], [2,3], [1,2] ]
Output: [-1, 0, 1]
Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.

Example 3:
Input: [ [1,4], [2,3], [3,4] ]
Output: [-1, 2, -1]
Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
"""


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    """
    Thoughts:
    1. sort intervals based on start time
    2. loop through intervals, for each interval, add it to a heap(smallest end time in head)
    3. if head of a heap ,say interval0, its end time is earlier than current interval's start time,
        then set interval0's next right interval as current interval. And pop out interval0.
    4. Do step3 until there is not any. Then back to step2(loop next)

    Time: O(n*logn)
    Space: O(n)
    """
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        ret = [-1]*len(intervals)
        li = [(intervals[i].start, intervals[i].end, i) for i in range(len(intervals))]
        li.sort()
        hp = []
        for each in li:
            # sort by first complete
            heapq.heappush(hp,(each[1],each[2],each[0]))
            #print(hp)
            while hp[0][0]<=each[0]:
                ret[heapq.heappop(hp)[1]] = each[2]
        return ret


# test
if __name__=="__main__":
    tmp = FindRightInterval()
    intervals = [
        Interval(2,4),
        Interval(2,3),
        Interval(1,2)
    ]
    result = tmp.findRightInterval(intervals)
    print(result)
