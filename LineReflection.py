"""
Given n points on a 2D plane,
find if there is such a line parallel to y-axis that reflect the given points.

Example 1:
Input: [[1,1],[-1,1]]
Output: true

Example 2:
Input: [[1,1],[-1,-1]]
Output: false

Follow up:
Could you do better than O(n^2) ?
"""
class Solution:
    def isReflected(self, points: 'List[List[int]]') -> 'bool':
        if len(points)==0:
            return True
        max_x, min_x = points[0][0], points[0][0]
        pointSet = set()
        pointSet.add(tuple(points[0]))
        for i in range(1,len(points)):
            max_x = max(max_x, points[i][0])
            min_x = min(min_x, points[i][0])
            pointSet.add(tuple(points[i]))
        mirror = (min_x+max_x)/2
        mm = set()
        for x,y in pointSet:
            if x==mirror:
                continue
            mirror_x = 2*mirror-x
            if (mirror_x, y) in mm:
                mm.remove((mirror_x,y))
            else:
                mm.add((x,y))
        return len(mm)==0
