"""
Given two words word1 and word2,
find the minimum number of steps required to make word1 and word2 the same,
where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Note:
1. The length of given words won't exceed 500.
2. Characters in given words can only be lower-case letters.
"""
class Solution:
    def minDistance(self, word1: 'str', word2: 'str') -> 'int':
        m, n = len(word1), len(word2)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        for i in range(n+1):
            dp[0][i] = i
        for i in range(1,m+1):
            dp[i][0] = i
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                if dp[i][j]==-1:
                    dp[i][j] = i+j
                dp[i][j] = min(dp[i][j], dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[m][n]
