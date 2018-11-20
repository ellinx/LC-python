"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:
1. The length of the given array is positive and will not exceed 20.
2. The sum of elements in the given array will not exceed 1000.
3. Your output answer is guaranteed to be fitted in a 32-bit integer.
"""
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        cur = dict()
        cur[0] = 1
        for num in nums:
            nxt = dict()
            for k in cur:
                nxt[k+num] = nxt.get(k+num, 0)+cur[k]
                nxt[k-num] = nxt.get(k-num, 0)+cur[k]
            cur = nxt
        return cur.get(S, 0)

class Solution2:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def helper(nums, start, S, mm):
            if S in mm[start]:
                return mm[start][S]
            ret = 0
            if start==len(nums)-1:
                if nums[start]==S:
                    ret += 1
                if -nums[start]==S:
                    ret += 1
                return ret
            ret += helper(nums, start+1, S-nums[start], mm)
            ret += helper(nums, start+1, S+nums[start], mm)
            mm[start][S] = ret
            return ret

        return helper(nums, 0, S, collections.defaultdict(dict))
