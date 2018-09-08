"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = None
        b = 1
        for i in range(len(s)):
            c = 0
            if s[i]!='0':
                c += b
            if i-1>=0 and a is not None and int(s[i-1:i+1])>=10 and int(s[i-1:i+1])<=26:
                c += a
            a, b = b, c
        return b
