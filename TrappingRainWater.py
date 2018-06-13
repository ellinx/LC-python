"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n<=2:
            return 0
        left, right = [0]*n, [0]*n
        for i in range(1, n):
            left[i] = max(left[i-1],height[i-1])
            right[n-1-i] = max(right[n-i], height[n-i])
        ret = 0
        for i in range(n):
            temp = min(left[i],right[i])-height[i]
            if temp>0:
                ret += temp
        return ret
