"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with a one-pass algorithm using only constant space?
"""
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index0 = 0
        while index0<len(nums) and nums[index0]==0:
            index0 += 1
        index2 = len(nums)-1
        while index2>=0 and nums[index2]==2:
            index2 -= 1
        index = index0
        while index<=index2:
            if nums[index]==0:
                if index0==index:
                    index0 += 1
                    index += 1
                else:
                    nums[index] = nums[index0]
                    nums[index0] = 0
                    index0 += 1
            elif nums[index]==1:
                index += 1
            else:
                nums[index] = nums[index2]
                nums[index2] = 2
                index2 -= 1
