"""
Given an array which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)

Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""
class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # sum of any subarray will fall into [max of the array, sum of the array]
        # use binary search to see if it's possible to cut array with m-1 cuts so that sum of each subarray is no greater than a given number
        def canCut(nums, target, cutNum):
            # greedy
            acc = 0
            for i in range(len(nums)):
                if acc+nums[i]<=target:
                    acc += nums[i]
                    continue
                cutNum -= 1
                if cutNum<0:
                    break
                acc = nums[i]
            return cutNum>=0

        if m==1:
            return sum(nums)
        left,right = max(nums),sum(nums)
        while left<=right:
            mid = left+(right-left)//2
            if canCut(nums, mid, m-1):
                right = mid-1
            else:
                left = mid+1
            #print(left,right)
        return left


class Solution2:
    def splitArray(self, nums: List[int], m: int) -> int:
        def dfs(nums, start, m, mm):
            if len(nums)-start<m:
                return -1
            if len(nums)-start==m:
                return max(nums[start:])
            if m==1:
                return sum(nums[start:])
            key = (start,m)
            if key in mm:
                return mm[key]
            total = 0
            for i in range(start,len(nums)-m+1):
                total += nums[i]
                after = dfs(nums, i+1, m-1, mm)
                if after==-1:
                    continue
                mm[key] = min(mm.get(key,float('inf')), max(total, after))
            if key not in mm:
                mm[key] = -1
            return mm[key]

        return dfs(nums, 0, m, dict())
