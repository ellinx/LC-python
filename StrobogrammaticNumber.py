"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:
Input:  "69"
Output: true

Example 2:
Input:  "88"
Output: true

Example 3:
Input:  "962"
Output: false
"""
class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        mm = {"0":"0","1":"1", "6":"9","8":"8","9":"6"}
        s, e = 0, len(num)-1
        while s<=e:
            if num[s] in mm and mm[num[s]]==num[e]:
                s += 1
                e -= 1
                continue
            return False
        return True
