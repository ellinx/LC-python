"""
Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points,
with sides not necessarily parallel to the x and y axes.

If there isn't any rectangle, return 0.


Example 1:
Input: [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.

Example 2:
Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.

Example 3:
Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.

Example 4:
Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.


Note:
1. 1 <= points.length <= 50
2. 0 <= points[i][0] <= 40000
3. 0 <= points[i][1] <= 40000
4. All points are distinct.
5. Answers within 10^-5 of the actual value will be accepted as correct.
"""
class Solution:
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        pSet = set()
        for x,y in points:
            pSet.add((x,y))
        ret = float('inf')
        n = len(points)
        for i in range(n):
            p1 = points[i]
            for j in range(n):
                if j==i:
                    continue
                p2 = points[j]
                for k in range(j+1,n):
                    if k==i:
                        continue
                    p3 = points[k]
                    p4 = [p2[0]+p3[0]-p1[0], p2[1]+p3[1]-p1[1]]
                    if tuple(p4) in pSet:
                        dotProduct = ((p2[0]-p1[0])*(p3[0]-p1[0])+(p2[1]-p1[1])*(p3[1]-p1[1]))
                        if dotProduct==0:
                            area = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)*math.sqrt((p3[0]-p1[0])**2+(p3[1]-p1[1])**2)
                            ret = min(ret, area)
        if ret==float('inf'):
            return 0
        return ret
