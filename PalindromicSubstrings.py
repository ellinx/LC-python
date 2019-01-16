"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings
even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:
The input string length won't exceed 1000.
"""
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for i in range(len(s)):
            l, r = i, i
            while l>=0 and r<len(s) and s[l]==s[r]:
                ret += 1
                l -= 1
                r += 1
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                ret += 1
                l -= 1
                r += 1
        return ret
