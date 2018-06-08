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

        #if nums1 is empty
        if m==0:
            return (nums2[(n-1)//2]+nums2[n//2])/2.0

        start, end = -1, m-1
        target = (m+n)//2
            #                   A
            #               mid | mid+1  ~[-1, m-1]
            #                   B
            #      target-mid-2 | target-mid-1  ~[-1, n-1]

        while start<=end:
            mid = start+(end-start)//2
            print(start, end, mid, target-mid-2)
            if mid==-1 or target-mid-1==n:
                if nums1[mid+1]>=nums2[target-mid-2]:
                    break
                else:
                    start = mid+1
                    continue
            if mid+1==m or target-mid-2==-1:
                if nums1[mid]<=nums2[target-mid-1]:
                    break
                else:
                    end = mid-1
                    continue

            if nums1[mid]>nums2[target-mid-1]:
                end = mid-1
            elif nums1[mid+1]<nums2[target-mid-2]:
                start = mid+1
            else:
                break
        #print(mid,target-mid-2)
        left, right = float('-inf'), float('inf')
        if (m+n)%2==0:
            if mid>=0:
                left = nums1[mid]
            if target-mid-2>=0:
                left = max(left, nums2[target-mid-2])
            if mid+1<m:
                right = nums1[mid+1]
            if target-mid-1<n:
                right = min(right, nums2[target-mid-1])
            return (left+right)/2.0
        else:
            if mid+1==m:
                return nums2[target-mid-1]
            if target-mid-1==n:
                return nums1[mid+1]
            return min(nums1[mid+1], nums2[target-mid-1])
