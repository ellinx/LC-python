"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m>n:
            return self.findMedianSortedArrays(nums2, nums1)
        l, r = -1, m-1
        #                   A
        #               i1-1 | i1  ~[-1, m-1]
        #                   B
        #               i2-1 | i2  ~[-1, n-1]
        while l<=r:
            mid = l+(r-l)//2
            i1 = mid+1
            i2 = (m+n)//2-i1
            if (i1-1<0 or i2>=n or nums1[i1-1]<=nums2[i2]) and (i1>=m or i2-1<0 or nums1[i1]>=nums2[i2-1]):
                break
            if i1-1>=0 and i2<n and nums1[i1-1]>nums2[i2]:
                r = mid-1
            elif i1<m and i2-1>=0 and nums1[i1]<nums2[i2-1]:
                l = mid+1
        #print(i1, i2)
        maxL, minR = float('-inf'), float('inf')
        if i1-1>=0 and i1-1<m:
            maxL = max(maxL, nums1[i1-1])
        if i2-1>=0 and i2-1<n:
            maxL = max(maxL, nums2[i2-1])
        if i1>=0 and i1<m:
            minR = min(minR, nums1[i1])
        if i2>=0 and i2<n:
            minR = min(minR, nums2[i2])
        if (m+n)%2==0:
            return (maxL+minR)/2
        return minR
