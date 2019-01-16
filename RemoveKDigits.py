"""
Given a non-negative integer num represented as a string,
remove k digits from the number so that the new number is the smallest possible.

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
    """
    DFS, each time remove one digit
    """
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        def removeDigit(numStr, k):
            if k>=len(numStr):
                return "0"
            if k==0:
                return numStr
            idx = 0
            while idx<len(numStr)-1:
                if numStr[idx]>numStr[idx+1]:
                    break
                idx += 1
            nxt = numStr[:idx]+numStr[idx+1:]
            idx = 0
            while idx<len(nxt) and nxt[idx]=='0':
                idx += 1
            nxt = nxt[idx:]
            return removeDigit(nxt, k-1)

        return removeDigit(num, k)


class Solution2:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stk = collections.deque()
        for c in num:
            while len(stk) and stk[-1]>c and k:
                stk.pop()
                k -= 1
            stk.append(c)
        ret = "".join(stk)
        idx = 0
        while idx<len(ret) and ret[idx]=='0':
            idx += 1
        ret = ret[idx:]
        if k>=len(ret):
            return "0"
        if k==0:
            return ret
        return ret[:-k]
