"""
Given a string representing an expression of fraction addition and subtraction,
you need to return the calculation result in string format.

The final result should be irreducible fraction.
If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1.
So in this case, 2 should be converted to 2/1.

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
1. The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
2. Each fraction (input and output) has format ±numerator/denominator.
    If the first input fraction or the output is positive, then '+' will be omitted.
3. The input only contains valid irreducible fractions,
    where the numerator and denominator of each fraction will always be in the range [1,10].
    If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
4. The number of given fractions will be in the range [1,10].
5. The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.

"""
class Solution:
    def fractionAddition(self, expression: 'str') -> 'str':
        def getGcd(a, b):
            while b!=0:
                a, b = b, a%b
            return a

        def add(f0, f1):
            ret = [0,1]
            gcd = getGcd(f0[1],f1[1])
            ret[1] = f0[1]//gcd*f1[1]
            ret[0] = f0[0]*(f1[1]//gcd)+f1[0]*(f0[1]//gcd)
            gcd = getGcd(ret[0],ret[1])
            return [ret[0]//gcd, ret[1]//gcd]

        sign = 1
        cur = [0,1]
        idx = 0
        while idx<len(expression):
            if expression[idx]=="+":
                sign = 1
                idx += 1
            elif expression[idx]=="-":
                sign = -1
                idx += 1
            else:
                temp = [0,1]
                end = idx+1
                while expression[end]!="/":
                    end += 1
                temp[0] = int(expression[idx:end])
                end += 1
                idx = end
                while end<len(expression) and expression[end].isdigit():
                    end += 1
                temp[1] = int(expression[idx:end])
                temp[0] *= sign
                cur = add(cur, temp)
                idx = end
        return str(cur[0])+"/"+str(cur[1])
