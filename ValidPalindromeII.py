"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(s):
            return s==s[::-1]

        start, end = 0, len(s)-1
        while start<=end:
            if s[start]!=s[end]:
                return isPalin(s[start:end]) or isPalin(s[start+1:end+1])
            start += 1
            end -= 1
        return True
