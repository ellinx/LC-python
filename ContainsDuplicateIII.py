"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false


"""

from typing import List
import bisect

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # similar idea of bucket sort
        def getIndex(num):
            if t==0:
                return num+2147483648
            return (num+2147483648)//t

        if k<=0 or t<0:
            return False
        buckets = dict()
        for i in range(len(nums)):
            if i>k:
                index = getIndex(nums[i-k-1])
                buckets.pop(index)
            index = getIndex(nums[i])
            # fall in same bucket
            if index in buckets:
                return True
            # check left adjant bucket
            if index-1 in buckets and nums[i]-buckets[index-1]<=t:
                return True
            # check right adjant bucket
            if index+1 in buckets and buckets[index+1]-nums[i]<=t:
                return True
            buckets[index] = nums[i]
        return False

class Solution2:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        def insertIndex(li, num):
            s, e = 0, len(li)-1
            while s<=e:
                m = s+(e-s)//2
                if li[m]==num:
                    return m
                if li[m]<num:
                    s = m+1
                else:
                    e = m-1
            return s

        li = []
        for i in range(len(nums)):
            #idx = insertIndex(li, nums[i])
            idx = bisect.bisect_left(li, nums[i])
            diff = float('inf')
            if idx-1>=0:
                diff = min(diff, nums[i]-li[idx-1])
            if idx<len(li):
                diff = min(diff, li[idx]-nums[i])
            if diff<=t:
                return True
            li.insert(idx, nums[i])
            if i>=k:
                li.remove(nums[i-k])
        return False


if __name__ == "__main__":
    test = Solution2()
    nums = [1,2,3,1]
    k, t = 3, 0
    print(test.containsNearbyAlmostDuplicate(nums, k, t))
