"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces .

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
    def calculate(self, s: 'str') -> 'int':
        stk = collections.deque()
        cur = 0
        sign = 1
        idx = 0
        while idx<len(s):
            if s[idx]==" ":
                idx += 1
                continue
            if s[idx]=="(":
                stk.append([cur,sign])
                cur, sign = 0, 1
                idx += 1
            elif s[idx]==")":
                temp = cur
                cur, sign = stk.pop()
                cur += sign*temp
                sign = 1
                idx += 1
            elif s[idx]=="+":
                idx += 1
            elif s[idx]=="-":
                sign = -1
                idx += 1
            elif s[idx].isdigit():
                end = idx+1
                while end<len(s) and s[end].isdigit():
                    end += 1
                cur += sign*int(s[idx:end])
                sign = 1
                idx = end
        return cur
