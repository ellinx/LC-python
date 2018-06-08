"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

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
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        # dp[i] is longest valid parentheses ends at i
        dp = [0]*len(s)
        for i in range(1,len(s)):
            if s[i]=="(":
                continue
            elif s[i]==")":
                if s[i-1]=="(":
                    if i-2>=0:
                        dp[i] = dp[i-2]+2
                    else:
                        dp[i] = 2
                else:
                    if i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=="(":
                        dp[i] = dp[i-1]+2
                        if i-dp[i-1]-2>=0:
                            dp[i] += dp[i-dp[i-1]-2]
            ret = max(ret, dp[i])
        return ret

    # def longestValidParentheses(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     invalidIndex = collections.deque()
    #     for i in range(len(s)):
    #         if s[i]=="(":
    #             invalidIndex.append(i)
    #         elif s[i]==")":
    #             if len(invalidIndex) and s[invalidIndex[-1]]=="(":
    #                 invalidIndex.pop()
    #             else:
    #                 invalidIndex.append(i)
    #     #print(invalidIndex)
    #     ret = 0
    #     pre = 0
    #     for each in invalidIndex:
    #         ret = max(ret, each-pre)
    #         pre = each+1
    #     ret = max(ret, len(s)-pre)
    #     return ret
