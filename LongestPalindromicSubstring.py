"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = "#"+"#".join(s)+"#"
        #print(s)
        ret = ""
        for i in range(len(s)):
            offset = 0
            while i-offset>=0 and i+offset<len(s) and s[i-offset]==s[i+offset]:
                offset += 1
            offset -= 1
            if s[i]=='#' and len(ret)<(offset//2)*2:
                #print(i, s[i-offset+1:i+offset])
                ret = "".join(s[i-offset+1:i+offset].split("#"))
            elif s[i]!='#' and len(ret)<(offset//2)*2+1:
                #print(i, s[i-offset+1:i+offset])
                ret = "".join(s[i-offset+1:i+offset].split("#"))
        return ret
