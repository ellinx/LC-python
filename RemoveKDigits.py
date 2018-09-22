"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""
class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k==0:
            return num
        if k>=len(num):
            return '0'
        stk = collections.deque()
        for i,c in enumerate(num):
            while len(stk)>0 and int(stk[-1])>int(c):
                if stk[-1]!='0':
                    stk.pop()
                    k -= 1
                    if k==0:
                        return str(int("".join(stk)+num[i:]))
            if c!='0':
                stk.append(c)
        #print(stk, k)
        ret = "".join(stk)[:-k]
        if ret=="":
            return '0'
        return ret
