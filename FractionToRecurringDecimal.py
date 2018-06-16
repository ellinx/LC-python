"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

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
        if numerator==0:
            return "0"
        sign1, sign2 = 1, 1
        if numerator<0:
            sign1 = -1
        if denominator<0:
            sign2 = -1
        if sign1==-1 or sign2==-1:
            if sign1==-1 and sign2==-1:
                return self.fractionToDecimal(-numerator, -denominator)
            return "-"+self.fractionToDecimal(sign1*numerator, sign2*denominator)
        ret = ""
        if numerator>=denominator:
            ret += str(numerator//denominator)
            numerator %= denominator
        else:
            ret = "0"
        if numerator==0:
            return ret
        ret += "."
        mem = dict()
        while numerator:
            nxt = numerator*10
            temp = nxt//denominator
            nxt %= denominator
            if ret[-1]=="." or numerator not in mem:
                ret += str(temp)
                mem[numerator] = len(ret)-1
                numerator = nxt
                continue
            if numerator in mem:
                ret = ret[:mem[numerator]]+"("+ ret[mem[numerator]:] +")"
                break
        return ret
