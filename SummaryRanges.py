"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.


"""
class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret = []
        if len(nums)==0:
            return ret
        cur = [nums[0], 1]
        for i in range(1,len(nums)):
            if cur[0]+cur[1]==nums[i]:
                cur[1] += 1
                continue
            if cur[1]==1:
                ret.append(str(cur[0]))
            else:
                ret.append(str(cur[0])+"->"+str(cur[0]+cur[1]-1))
            cur = [nums[i], 1]
        if cur[1]==1:
            ret.append(str(cur[0]))
        else:
            ret.append(str(cur[0])+"->"+str(cur[0]+cur[1]-1))
        return ret
