"""
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"


"""
class Solution:
    def longestValidParentheses(self, s: 'str') -> 'int':
        n = len(s)
        ret = 0
        # dp[i] is longest valid parentheses ends at i
        dp = [0]*n
        for i in range(n):
            if s[i]=="(":
                continue
            if i-1>=0 and i-1-dp[i-1]>=0 and s[i-1-dp[i-1]]=="(":
                dp[i] = dp[i-1]+2
                if i-1-dp[i-1]-1>=0:
                    dp[i] += dp[i-1-dp[i-1]-1]
                ret = max(ret, dp[i])
        return ret

class Solution2:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        invalidIndex = collections.deque()
        for i in range(len(s)):
            if s[i]=="(":
                invalidIndex.append(i)
            elif s[i]==")":
                if len(invalidIndex) and s[invalidIndex[-1]]=="(":
                    invalidIndex.pop()
                else:
                    invalidIndex.append(i)
        #print(invalidIndex)
        ret = 0
        pre = 0
        for each in invalidIndex:
            ret = max(ret, each-pre)
            pre = each+1
        ret = max(ret, len(s)-pre)
        return ret
