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
class ReverseWordsInString(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, 0
        stk = []
        s = s.strip()
        while end<len(s):
            if s[end]!=' ':
                end += 1
                continue
            stk.append(s[start:end])
            while end<len(s) and s[end]==' ':
                end += 1
            start = end
        if start<len(s):
            stk.append(s[start:end])
        ret = ''
        for each in reversed(stk):
            ret += each+' '
        return ret[:-1]
