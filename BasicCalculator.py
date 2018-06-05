"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:
Input: "1 + 1"
Output: 2

Example 2:
Input: " 2-1 + 2 "
Output: 3

Example 3:
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = collections.deque()
        ret = 0
        sign = 1
        index = 0
        while index<len(s):
            if s[index]==" ":
                index += 1
                continue
            if s[index]=="+" or s[index]=="-":
                sign = 1 if s[index]=="+" else -1
                index += 1
            elif s[index]=="(":
                stk.append(ret)
                stk.append(sign)
                ret, sign = 0, 1
                index += 1
            elif s[index]==")":
                sign = stk.pop()
                ret = stk.pop()+sign*ret
                index += 1
            else:
                end = index+1
                while end<len(s) and s[end].isdigit():
                    end += 1
                ret += sign*int(s[index:end])
                index = end
            #print(stk,ret)
        return ret
