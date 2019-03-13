"""
Given the coordinates of four points in 2D space,
return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

Note:
1. All the input integers are in the range [-10000, 10000].
2. A valid square has four equal sides with positive length and four equal angles (90-degree angles).
3. Input points have no order.
"""
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def check(p1, p2, p3, p4):
            v1 = [p2[0]-p1[0], p2[1]-p1[1]]
            v2 = [p3[0]-p1[0], p3[1]-p1[1]]
            if v1[0]*v2[0]+v1[1]*v2[1]!=0:
                return False
            if v1[0]**2+v1[1]**2!=v2[0]**2+v2[1]**2:
                return False
            m1 = [(p1[0]+p4[0])/2, (p1[1]+p4[1])/2]
            m2 = [(p2[0]+p3[0])/2, (p2[1]+p3[1])/2]
            return m1==m2

        points = set([tuple(p1),tuple(p2),tuple(p3),tuple(p4)])
        if len(points)<4:
            return False
        return check(p1,p2,p3,p4) or check(p1,p4,p2,p3) or check(p1,p4,p3,p2)
