"""
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points,
with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.


Example 1:
Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Example 2:
Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2


Note:
1. 1 <= points.length <= 500
2. 0 <= points[i][0] <= 40000
3. 0 <= points[i][1] <= 40000
4. All points are distinct.
"""
class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        mm = collections.defaultdict(set)
        for x,y in points:
            mm[x].add(y)
        ret = 0
        for i in range(n-1):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2, y2 = points[j]
                if x1==x2 or y1==y2:
                    continue
                if y1 in mm[x2] and y2 in mm[x1]:
                    ret = abs(x1-x2)*abs(y1-y2) if ret==0 else min(ret, abs(x1-x2)*abs(y1-y2))
        return ret
