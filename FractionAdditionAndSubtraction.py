"""
Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format.
The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:

Input:"-1/2+1/2"
Output: "0/1"

Example 2:

Input:"-1/2+1/2+1/3"
Output: "1/3"

Example 3:

Input:"1/3-1/2"
Output: "-1/6"

Example 4:

Input:"5/3+1/3"
Output: "2/1"

Note:

    The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
    Each fraction (input and output) has format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
    The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
    The number of given fractions will be in the range [1,10].
    The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.

"""
class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        # calculate sum of two fractions
        def cal(s1, s2):
            ret = [""]*2
            s1 = s1.split("/")
            s2 = s2.split("/")
            if s1[1]==s2[1]:
                ret[0] = int(s1[0])+int(s2[0])
                ret[1] = int(s1[1])
            else:
                ret[0] = int(s1[0])*int(s2[1])+int(s2[0])*int(s1[1])
                ret[1] = int(s1[1])*int(s2[1])
            gcd = math.gcd(ret[0],ret[1])
            return str(ret[0]//gcd)+"/"+str(ret[1]//gcd)

        ret = "0/1"
        start, end = 0, 0
        while end<len(expression):
            if start!=end and (expression[end]=="+" or expression[end]=="-"):
                ret = cal(ret, expression[start:end])
                start = end
                continue
            end += 1
        return cal(ret, expression[start:end])
