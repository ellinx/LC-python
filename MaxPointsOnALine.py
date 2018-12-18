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
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        points.sort(key=lambda p:p.x)
        ret = 0
        for i in range(len(points)):
            sameP = 1
            sameX = 0
            kdict = dict()
            for j in range(i+1,len(points)):
                if points[i].x==points[j].x:
                    if points[i].y==points[j].y:
                        sameP += 1
                    else:
                        sameX += 1
                    continue
                deltaY = points[j].y-points[i].y
                deltaX = points[j].x-points[i].x
                tmp = gcd(deltaY, deltaX)
                k = str(deltaY//tmp)+","+str(deltaX//tmp)
                kdict[k] = kdict.get(k, sameP)+1
                ret = max(ret, kdict[k])
            ret = max(ret, sameX+sameP)
        return ret
