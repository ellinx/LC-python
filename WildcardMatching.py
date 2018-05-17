"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""

class WildcardMatching:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s)+1, len(p)+1
        dp = [[False]*n for _ in range(m)]
        pre = [False]*n
        dp[0][0] = True
        pre[0] = True
        for i in range(1,n):
            dp[0][i] = dp[0][i-1] and p[i-1]=='*'
            pre[i] = dp[0][i]
        for i in range(1,m):
            for j in range(1,n):
                if p[j-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j] = pre[j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1]==p[j-1]
                pre[j] = pre[j] or dp[i][j]
        #print(dp)
        return dp[m-1][n-1]