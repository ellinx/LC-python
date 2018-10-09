"""
Given an input string, reverse the string word by word.

Example:

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        l, r = 0, 0
        while r<len(s):
            while l<len(s):
                if s[l]==' ':
                    l += 1
                    continue
                break
            if l==len(s):
                break
            r = l
            while r<len(s):
                if s[r]!=' ':
                    r += 1
                    continue
                break
            words.append(s[l:r])
            l = r+1
        return ' '.join(words[::-1])
