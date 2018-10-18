"""
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9

Example 2:
Input: N = 1234
Output: 1234

Example 3:
Input: N = 332
Output: 299

Note: N is an integer in the range [0, 10^9].
"""
class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        def helper(s):
            if len(s)==1:
                return str(int(s)-1)
            for i in range(len(s)-1,-1,-1):
                if i==0 or int(s[i-1])<=int(s[i])-1:
                    break
            ret = ""
            for idx in range(i):
                ret += s[idx]
            ret += str(int(s[i])-1)
            for idx in range(i+1,len(s)):
                ret += '9'
            return ret

        ret = ""
        strN = str(N)
        for i,c in enumerate(strN):
            if i==0 or int(strN[i-1])<=int(c):
                ret += c
                continue
            break
        if len(ret)==len(strN):
            return int(ret)
        return int(helper(ret)+'9'*(len(strN)-i))
