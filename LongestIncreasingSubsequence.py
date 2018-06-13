"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Note:

    There may be more than one LIS combination, it is only necessary for you to return the length.
    Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

"""
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def insertIndex(seq, num):
            start, end = 0, len(seq)-1
            while start<=end:
                mid = start+(end-start)//2
                if seq[mid]==num:
                    return mid
                if seq[mid]<num:
                    start = mid+1
                else:
                    end = mid-1
            return start

        if len(nums)==0:
            return 0
        seq = [nums[0]]
        for i in range(1,len(nums)):
            index = insertIndex(seq, nums[i])
            if index==len(seq):
                seq.append(nums[i])
                continue
            if seq[index]==nums[i]:
                continue
            seq[index] = nums[i]
        return len(seq)
