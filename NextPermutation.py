"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""
class Solution:
    """
    Thoughts:
    1. start from right side find a digit which is greater than its next left digit; if no such digit(it's descending order, now put as ascending number)
    2. find the smallest digit which is greater than the digit we find above
    3. swap these two digit and sort all digit right from first swap digit to ascending order

    Time: O(n*logn) where n is length of list
    Space: O(1)
    """
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #
        #
        #
        index1 = len(nums)-2
        while index1>=0:
            if nums[index1]<nums[index1+1]:
                break
            index1 -= 1
        if index1<0:
            return nums.sort()
        if index1==len(nums)-2:
            nums[index1], nums[index1+1] = nums[index1+1], nums[index1]
            return
        swap = min(list(filter(lambda x:x>nums[index1], nums[index1+1:])))
        index2 = len(nums)-1
        while index2>index1:
            if nums[index2]==swap:
                break
            index2 -= 1
        nums[index1], nums[index2] = nums[index2], nums[index1]
        nums[index1+1:] = sorted(nums[index1+1:])
