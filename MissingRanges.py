"""
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper],
return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
"""
class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ret = []
        start = lower
        for i in range(len(nums)):
            if start==nums[i]:
                start += 1
                continue
            if start<nums[i]:
                tmp = str(start)
                if start<nums[i]-1:
                    tmp += "->"+str(nums[i]-1)
                ret.append(tmp)
                start = nums[i]+1
        if start<=upper:
            tmp = str(start)
            if start<upper:
                tmp += "->"+str(upper)
            ret.append(tmp)
        return ret
