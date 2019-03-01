"""
Given a list of 24-hour clock time points in "Hour:Minutes" format,
find the minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1

Note:
1. The number of time points in the given list is at least 2 and won't exceed 20000.
2. The input time is legal and ranges from 00:00 to 23:59.
"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(s):
            data = s.split(":")
            return int(data[0])*60+int(data[1])

        li = sorted(map(convert, timePoints))
        ret = float('inf')
        TOTAL = 24*60
        for i in range(1,len(li)):
            diff = li[i]-li[i-1]
            ret = min(ret, diff, TOTAL-diff)
        diff = li[-1]-li[0]
        ret = min(ret, diff, TOTAL-diff)
        return ret
