"""
There are a number of spherical balloons spread in two-dimensional space.
For each balloon, provided input is the start and end coordinates of the horizontal diameter.
Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start
and end of the diameter suffice. Start is always smaller than end. There will be at most 10^4 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis.
A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend.
There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely.
The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and
another arrow at x = 11 (bursting the other two balloons).
"""
class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # sort balloon based on end
        # short at the end to see how many following balloons can be skipped
        #
        if len(points)==0:
            return 0
        points.sort(key=lambda x:x[1])
        ret = 1
        idx = 0
        while idx<len(points):
            end = idx+1
            while end<len(points) and points[end][0]<=points[idx][1]:
                end += 1
            if end==len(points):
                break
            idx = end
            ret += 1
        return ret


# test
if __name__=="__main__":
    tmp = Solution()
    points = [[10,16], [2,8], [1,6], [7,12]]
    result = tmp.findMinArrowShots(points)
    print(result)
