"""
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
1. Each element in the result should appear as many times as it shows in both arrays.
2. The result can be in any order.

Follow up:
1. What if the given array is already sorted? How would you optimize your algorithm?
2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
3. What if elements of nums2 are stored on disk, and the memory is limited such that
    you cannot load all elements into the memory at once?
"""
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter = collections.Counter(nums1)
        ret = []
        for num in nums2:
            if counter.get(num, 0):
                ret.append(num)
                counter[num] -= 1
        return ret
