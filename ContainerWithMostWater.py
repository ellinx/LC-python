"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
class ContainerWithMostWater:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # starting from widest, ie 0-n
        # only higher narrow can be candidates
        left, right = 0, len(height)-1
        ret = 0
        while left<right:
            #print(left,right)
            h = min(height[left],height[right])
            ret = max(ret, h*(right-left))
            while left<right and height[left]<=h:
                left += 1
            while right>left and height[right]<=h:
                right -= 1
        return ret
