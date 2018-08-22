"""
 Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

1. 0 < i, i + 1 < j, j + 1 < k < n - 1
2. Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.

where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.

Example:

Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5.
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1

Note:

    1 <= n <= 2000.
    Elements in the given array will be in range [-1,000,000, 1,000,000].

"""
class Solution:
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(nums, cur, target, mm):
            total = 0
            index = cur[-1]+1
            key = str(index)+","+str(target)
            if key in mm:
                return mm[key]
            nxt = []
            #print(cur, target)
            if len(cur)==3:
                mm[key] = target==sum(nums[index:])
                return mm[key]
            while index<len(nums):
                total += nums[index]
                index += 1
                if total==target:
                    nxt.append(index)
            if len(nxt)==0:
                mm[key] = False
                return False
            for index in nxt:
                cur.append(index)
                if len(cur)<=3 and index<len(nums):
                    if dfs(nums, cur, target, mm):
                        mm[key] = True
                        return True
                cur.pop()
            mm[key] = False
            return False

        if len(nums)<7:
            return False
        total = nums[0]
        mm = dict()
        for i in range(1,len(nums)-4):
            if dfs(nums, [i], total, mm):
                return True
            total += nums[i]
        return False
