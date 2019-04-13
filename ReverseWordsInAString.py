"""
Given an input string, reverse the string word by word.

Example:

Input: "the sky is blue",
Output: "blue is sky the".

Note:
1. A word is defined as a sequence of non-space characters.
2. Input string may contain leading or trailing spaces.
    However, your reversed string should not contain leading or trailing spaces.
3. You need to reduce multiple spaces between two words to a single space in the reversed string.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        l, r = 0, 0
        while l<len(s):
            while l<len(s) and s[l]==" ":
                l += 1
            if l==len(s):
                break
            r = l
            while r<len(s) and s[r]!=" ":
                r += 1
            words.append(s[l:r])
            l = r+1
        return " ".join(words[::-1])
