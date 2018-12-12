"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
For the purpose of this problem, assume that your function returns 2^31 − 1 when the division result overflows.
"""
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        max_int = 2**31-1
        min_int = -2**31
        sign = 1
        if dividend==0:
            return 0
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            sign = -1
        dividend, divisor = abs(dividend), abs(divisor)
        mm = [divisor]
        while mm[-1]<dividend:
            mm.append(mm[-1]<<1)
        #print(mm)
        ret = 0
        while dividend>=divisor:
            idx = bisect.bisect_left(mm, dividend)
            if mm[idx]==dividend:
                ret += 2**idx
                break
            if idx==0:
                break
            ret += 2**(idx-1)
            dividend -= mm[idx-1]
        ret *= sign
        if ret>max_int:
            return max_int
        if ret<min_int:
            return min_int
        return ret
