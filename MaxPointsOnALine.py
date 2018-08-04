from Point import Point
"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4

Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
"""
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def getGCD(a, b):
            while b>0:
                a, b = b, a%b
            return a

        if len(points)<2:
            return len(points)
        points.sort(key=lambda p: [p.x,p.y])
        ret = 2
        for i in range(len(points)):
            if i and points[i-1].x==points[i].x and points[i-1].y==points[i].y:
                continue
            same = 1
            sameX = 0
            mm = collections.defaultdict(int)
            for j in range(i+1,len(points)):
                if points[j].x==points[i].x and points[j].y==points[i].y:
                    same += 1
                    ret = max(ret, same)
                    continue
                if points[j].x==points[i].x:
                    sameX += 1
                    ret = max(ret, sameX+same)
                    continue
                dy = points[j].y-points[i].y
                dx = points[j].x-points[i].x
                gcd = getGCD(dy,dx)
                k = (dy//gcd,dx//gcd)
                mm[k] += 1
                ret = max(ret, mm[(k)]+same)
        return ret
