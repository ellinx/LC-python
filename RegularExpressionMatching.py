"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Note:
1. s could be empty and contains only lowercase letters a-z.
2. p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1,n+1):
            if p[i-1]=="*":
                dp[0][i] = dp[0][i-2]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==p[j-1] or p[j-1]==".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=="*":
                    if s[i-1]==p[j-2] or p[j-2]==".":
                        # * match zero, one or more characters
                        dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]
                    else:
                        # * only match zero character
                        dp[i][j] = dp[i][j-2]
        return dp[m][n]
