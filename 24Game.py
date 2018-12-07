"""
You have 4 cards each containing a number from 1 to 9.
You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24

Example 2:
Input: [1, 2, 1, 2]
Output: False

Note:
1. The division operator / represents real division, not integer division.
    For example, 4 / (1 - 2/3) = 12.
2. Every operation done is between two numbers.
    In particular, we cannot use - as a unary operator.
    For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
3. You cannot concatenate numbers together.
    For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
"""
class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n==1:
            return abs(nums[0]-24)<0.001
        for i in range(n-1):
            for j in range(i+1,n):
                nxt = nums[:i]+nums[i+1:j]+nums[j+1:]
                if self.judgePoint24(nxt+[nums[i]+nums[j]]):
                    return True
                if self.judgePoint24(nxt+[nums[i]*nums[j]]):
                    return True
                if self.judgePoint24(nxt+[nums[i]-nums[j]]):
                    return True
                if self.judgePoint24(nxt+[nums[j]-nums[i]]):
                    return True
                if nums[j]!=0 and self.judgePoint24(nxt+[nums[i]/nums[j]]):
                    return True
                if nums[i]!=0 and self.judgePoint24(nxt+[nums[j]/nums[i]]):
                    return True
        return False
