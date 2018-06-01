"""
Given an input string , reverse the string word by word.

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Note:
A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""
class Solution:
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        def reverseHelper(s, start, end):
            while start<end:
                str[start],str[end] = str[end],str[start]
                start += 1
                end -= 1

        # reverse whole list then reverse each word
        if not len(str):
            return
        reverseHelper(str, 0, len(str)-1)
        start = 0
        while str[start]==' ':
            start += 1
        end = start
        while end<len(str):
            while end<len(str) and str[end]!=' ':
                end += 1
            reverseHelper(str, start,end-1)
            if end==len(str):
                break
            while end<len(str) and str[end]==' ':
                end += 1
            start = end
