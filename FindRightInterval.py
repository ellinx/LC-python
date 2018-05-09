"""
Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

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


from Interval import *


class FindRightInterval:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """

        if len(intervals) == 0:
            return 0

        list = []
        res = []
        for i in range(len(intervals)):
            list.append((intervals[i].start, i))

        list.sort()

        print(list)

        for interval in intervals:
            cur = interval.end

            # use binary search to find the index of intervals which has min start greater than cur
            start = 0
            end = len(intervals)-1
            index = -1
            while start <= end:
                if start == end:
                    if cur <= list[start][0]:
                        index = list[start][1]
                        break

                mid = start + (end-start)//2
                if cur <= list[mid][0]:
                    index = list[mid][1]
                    end = mid-1
                else:
                    start = mid+1

            res.append(index)

        return res


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