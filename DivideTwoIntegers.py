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
class DivideTwoIntegers:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        def insertPos(nums, target):
            start, end = 0, len(nums)-1
            while start<=end:
                mid = start+(end-start)//2
                if nums[mid]==target:
                    start=mid
                    break
                if nums[mid]>target:
                    end = mid-1
                else:
                    start = mid+1
            return start

        if dividend==0:
            return 0
        sign = 1
        if dividend>0 and divisor<0:
            sign, divisor = -1, -1*divisor
        elif dividend<0 and divisor>0:
            sign, dividend = -1, -1*dividend
        elif dividend<0 and divisor<0:
            dividend, divisor = -1*dividend, -1*divisor
        ret = 0
        bitmap = [divisor*2**i for i in range(32)]
        #print(bitmap)
        #print(dividend)
        while True:
            pos = insertPos(bitmap, dividend)
            if pos>31:
                ret = 2**31
                break
            if bitmap[pos]==dividend:
                ret |= 1<<pos
                break
            if pos==0:
                break
            ret |= 1<<(pos-1)
            dividend -= bitmap[pos-1]
        if sign==1 and ret>=2**31:
            return 2**31-1
        if sign==-1 and ret>2**31:
            return -1*2**31
        return sign*ret
