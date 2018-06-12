"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false


"""
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end =  0, len(s)-1
        while start<end:
            while start<len(s) and not s[start].isalnum():
                start += 1
            while end>=0 and not s[end].isalnum():
                end -= 1
            if start>=end:
                break
            if s[start].upper()!=s[end].upper():
                return False
            start += 1
            end -= 1
        return True
