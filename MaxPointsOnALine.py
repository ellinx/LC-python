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

class MaxPointsOnALine:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def calGcd(n1, n2):
            while n2:
                n1, n2 = n2, n1%n2
            return n1

        ret = 0
        if len(points)<=1:
            return len(points)
        for i in range(len(points)):
            same, v = 1, 0
            counter = collections.defaultdict(int)
            for j in range(i+1,len(points)):
                if points[i].x==points[j].x:
                    if points[i].y==points[j].y:
                        same += 1
                    else:
                        v += 1
                else:
                    # use Greatest common divisor to be more precise
                    #k = (points[i].y-points[j].y)/(points[i].x-points[j].x)
                    gcd = calGcd(points[i].y-points[j].y, points[i].x-points[j].x)
                    k = ((points[i].y-points[j].y)/gcd, (points[i].x-points[j].x)/gcd)
                    counter[k] += 1
            #print(counter)
            ret = max(ret,max([counter[k] for k in counter]+[v])+same)
        return ret
