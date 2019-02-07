"""
Solve a given equation and return the value of x in the form of string "x=#value".
The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"

Example 2:
Input: "x=x"
Output: "Infinite solutions"

Example 3:
Input: "2x=x"
Output: "x=0"

Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"

Example 5:
Input: "x=x+2"
Output: "No solution"
"""
class Solution:
    def solveEquation(self, equation: 'str') -> 'str':
        def process(s):
            ret = [0,0]
            sign = 1
            idx = 0
            while idx<len(s):
                if s[idx]=="+":
                    idx += 1
                elif s[idx]=="-":
                    sign = -1
                    idx += 1
                else:
                    if s[idx]=="x":
                        ret[0] += sign
                        idx += 1
                        sign = 1
                        continue
                    end = idx+1
                    while end<len(s) and s[end].isdigit():
                        end += 1
                    num = int(s[idx:end])
                    if end<len(s) and s[end]=="x":
                        ret[0] += sign*num
                        idx = end+1
                    else:
                        ret[1] += sign*num
                        idx = end
                    sign = 1
            return ret

        left, right = equation.split("=")
        lexp, rexp = process(left), process(right)
        #print(lexp, rexp)
        # ax=b
        a = lexp[0]-rexp[0]
        b = rexp[1]-lexp[1]
        if a==0:
            if b==0:
                return "Infinite solutions"
            return "No solution"
        return "x="+str(b//a)
