"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
1. You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
2. 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

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
        def dfs(B, l, r, mm):
            if l+1==r:
                return 0
            if (l,r) in mm:
                return mm[(l,r)]
            ret = 0
            for i in range(l+1,r):
                temp = B[l]*B[i]*B[r]
                temp += dfs(B,l,i,mm)+dfs(B,i,r,mm)
                ret = max(ret, temp)
            mm[(l,r)] = ret
            return ret

        B = [1]+nums+[1]
        return dfs(B,0,len(B)-1, dict())
