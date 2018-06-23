"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

    You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
    0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167


"""
class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #use last burst ballon instead of first burst balloon
        def dfs(nums, left, right, mem):
            if right-left==1:
                return 0
            if mem[left][right]:
                return mem[left][right]
            ret = 0
            for i in range(left+1,right):
                ret = max(ret, nums[left]*nums[i]*nums[right]+dfs(nums,left,i,mem)+dfs(nums,i,right,mem))
            mem[left][right] = ret
            return ret

        nums = [1]+nums+[1]
        mem = [[0]*len(nums) for _ in range(len(nums))]
        return dfs(nums, 0, len(nums)-1, mem)
