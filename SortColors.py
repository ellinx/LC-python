"""
Given an array with n objects colored red, white or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

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
        index0, index2 = 0, len(nums)-1
        index = 0
        while index<=index2:
            if nums[index]==1:
                index += 1
            elif nums[index]==0:
                if index==index0:
                    index += 1
                    index0 += 1
                else:
                    nums[index0], nums[index] = nums[index], nums[index0]
                    index0 += 1
            else:
                nums[index], nums[index2] = nums[index2], nums[index]
                index2 -= 1
