"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

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
        n = len(s)
        ret = ""
        for i in range(n):
            if len(ret)>=1+2*(n-i-1):
                break
            # odd
            l, r = i-1, i+1
            while l>=0 and r<n and s[l]==s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            if len(ret)<r-l+1:
                ret = s[l:r+1]
            # even
            if i+1<n and s[i]==s[i+1]:
                l, r = i, i+1
                while l>=0 and r<n and s[l]==s[r]:
                    l -= 1
                    r += 1
                l += 1
                r -= 1
                if len(ret)<r-l+1:
                    ret = s[l:r+1]
        return ret
