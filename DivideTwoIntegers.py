"""
Given two integers dividend and divisor, divide two integers without using multiplication,
division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

Note:
1. Both dividend and divisor will be 32-bit signed integers.
2. The divisor will never be 0.
3. Assume we are dealing with an environment which could only store integers
    within the 32-bit signed integer range: [−2^31,  2^31 − 1].
4. For the purpose of this problem, assume that your function returns 2^31 − 1 when the division result overflows.
"""
class Solution:
    def divide(self, dividend: 'int', divisor: 'int') -> 'int':
        if dividend==0:
            return 0
        MAX_INT, MIN_INT = 2**31-1, -2**31
        #print(MAX_INT, MIN_INT)
        sign = 1
        if dividend<0:
            dividend = -dividend
            sign *= -1
        if divisor<0:
            divisor = -divisor
            sign *= -1
        ret = 0
        mm = [divisor]
        while dividend>=divisor:
            while dividend>mm[-1]:
                mm.append(mm[-1]*2)
            idx = bisect.bisect_left(mm, dividend)
            if dividend==mm[idx]:
                ret += 2**idx
                dividend = 0
            else:
                ret += 2**(idx-1)
                dividend -= mm[idx-1]
            if sign*ret>MAX_INT or sign*ret<MIN_INT:
                return MAX_INT
        return sign*ret
