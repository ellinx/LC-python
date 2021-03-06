"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces.
The integer division should truncate toward zero.

Example 1:
Input: "3+2*2"
Output: 7

Example 2:
Input: " 3/2 "
Output: 1

Example 3:
Input: " 3+5 / 2 "
Output: 5

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
        index = 0
        while index<len(s):
            if s[index]==" ":
                index += 1
                continue
            if s[index]=="+" or s[index]=="-" or s[index]=="*" or s[index]=="/":
                stk.append(s[index])
                index += 1
            else:
                end = index+1
                while end<len(s) and s[end].isdigit():
                    end += 1
                cur = int(s[index:end])
                if len(stk) and (stk[-1]=="*" or stk[-1]=="/"):
                    op = stk.pop()
                    pre = stk.pop()
                    if op=="*":
                        stk.append(pre*cur)
                    else:
                        stk.append(pre//cur)
                else:
                    stk.append(cur)
                index = end
        ret, sign = 0, 1
        for each in stk:
            if each=="+":
                sign = 1
            elif each=="-":
                sign = -1
            else:
                ret += sign*each
        return ret

class Solution2:
    def calculate(self, s: 'str') -> 'int':
        cur, last, sign = 0, 0, "+"
        idx = 0
        while idx<len(s):
            if s[idx]==" ":
                idx += 1
                continue
            if s[idx] in "+-*/":
                sign=s[idx]
                idx += 1
            elif s[idx].isdigit():
                end = idx+1
                while end<len(s) and s[end].isdigit():
                    end += 1
                num = int(s[idx:end])
                idx = end
                #print(cur, last, sign, num)
                if sign=="+":
                    cur += num
                    last = num
                elif sign=="-":
                    cur -= num
                    last = -num
                elif sign=="*":
                    cur -= last
                    cur += last*num
                    last = last*num
                else:
                    cur -= last
                    cur += int(last/num)
                    last = int(last/num)
        return cur
