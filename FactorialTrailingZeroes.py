"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.

"""
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # count number of factor 5
        # count 5^1, 5^2,...
        ret = 0
        i = 5
        while i<=n:
            ret += n//i
            i *= 5
        return ret
