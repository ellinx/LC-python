"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces.

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces. 
The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12


Note: Do not use the eval built-in library function.
"""
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # function to process a number
        def processNum(stk, num):
            if len(stk) and (stk[-1]=="*" or stk[-1]=="/"):
                op = stk.pop()
                pre = stk.pop()
                if op=="*":
                    stk.append(pre*num)
                else:
                    stk.append(pre//num)
            else:
                stk.append(num)

        #function to calculate a () pair
        def calHelper(s, start):
            # return (result, nextIndex)
            stk = collections.deque()
            while start<len(s):
                #print(stk,start)
                if s[start]==" ":
                    start += 1
                    continue
                if s[start]=="(":
                    cur, start = calHelper(s,start+1)
                    processNum(stk, cur)
                elif s[start]=="+" or s[start]=="-" or s[start]=="*" or s[start]=="/":
                    stk.append(s[start])
                    start += 1
                elif s[start]==")":
                    start += 1
                    break
                else:
                    end = start+1
                    while end<len(s) and s[end].isdigit():
                        end += 1
                    cur = int(s[start:end])
                    start = end
                    processNum(stk, cur)
            ret, sign = 0, 1
            #print(stk)
            for each in stk:
                if each=="+":
                    sign = 1
                elif each=="-":
                    sign = -1
                else:
                    ret += sign*each
            #print(ret,start)
            return (ret,start)

        # assume whole string has a pair of ()
        return calHelper(s,0)[0]
