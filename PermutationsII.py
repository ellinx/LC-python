"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, cur, used, ret):
            if len(cur)==len(nums):
                ret.append(cur)
                return
            pre = None
            for i in range(len(nums)):
                if not used[i]:
                    if pre is None or pre!=nums[i]:
                        used[i] = True
                        dfs(nums, cur+[nums[i]], used, ret)
                        pre = nums[i]
                        used[i] = False

        nums.sort()
        ret = []
        if len(nums)==0:
            return ret
        dfs(nums, [], [False]*len(nums), ret)
        return ret


class Solution2:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(n, arr, cur, ret):
            if len(cur)==n:
                ret.append(cur)
                return
            for i in range(len(arr)):
                if arr[i][1]:
                    arr[i][1] -= 1
                    dfs(n, arr, cur+[arr[i][0]],ret)
                    arr[i][1] += 1

        n = len(nums)
        counter = collections.Counter(nums)
        arr = list(map(list,counter.items()))
        ret = []
        for i in range(len(arr)):
            arr[i][1] -= 1
            dfs(n, arr, [arr[i][0]],ret)
            arr[i][1] += 1
        return ret
