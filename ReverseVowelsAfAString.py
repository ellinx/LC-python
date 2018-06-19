"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y". 
"""
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = collections.deque()
        for c in s:
            low = c.lower()
            if low=='a' or low=='e' or low=='i' or low=='o' or low=='u':
                stk.append(c)
        ret = ""
        for c in s:
            low = c.lower()
            if low=='a' or low=='e' or low=='i' or low=='o' or low=='u':
                ret += stk.pop()
            else:
                ret += c
        return ret
