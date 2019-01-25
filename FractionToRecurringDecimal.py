"""
Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 2, denominator = 3
Output: "0.(6)"

"""
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ret = ""
        sign = "+"
        if numerator/denominator<0:
            sign = "-"
        numerator, denominator = abs(numerator), abs(denominator)
        if numerator>=denominator:
            ret += str(numerator//denominator)
            numerator %= denominator
        else:
            ret = "0"
        if numerator==0:
            if sign=="-":
                return sign+ret
            return ret
        ret += "."
        mp = dict()
        idx = len(ret)
        while True:
            if numerator in mp:
                ret = ret[:mp[numerator]]+"("+ret[mp[numerator]:]+")"
                if sign=="-":
                    return sign+ret
                return ret
            mp[numerator] = idx
            idx += 1
            ret += str((numerator*10)//denominator)
            numerator = (numerator*10)%denominator
            if numerator==0:
                break
        if sign=="-":
            return sign+ret
        return ret
