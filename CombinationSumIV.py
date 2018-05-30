"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.
Therefore the output is 7.

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""
class CombinationSumIV:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def dfs(nums, target, count):
            if target in count:
                return count[target]
            if target==0:
                return 1
            ret = 0
            for num in nums:
                if target<num:
                    break
                ret += dfs(nums, target-num, count)
            count[target] = ret
            return ret

        nums.sort()
        return dfs(nums,target,dict())
