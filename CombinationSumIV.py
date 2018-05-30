"""

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
