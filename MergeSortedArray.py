"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index1,index2 = m-1, n-1
        index = m+n-1
        while index1>=0 and index2>=0:
            if nums1[index1]<=nums2[index2]:
                nums1[index] = nums2[index2]
                index -= 1
                index2 -=1
            else:
                nums1[index] = nums1[index1]
                index -= 1
                index1 -=1
        while index2>=0:
            nums1[index] = nums2[index2]
            index -= 1
            index2 -= 1
