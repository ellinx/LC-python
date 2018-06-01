"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        indexa, indexb = len(a)-1,len(b)-1
        carry = 0
        ret = ''
        while indexa>=0 and indexb>=0:
            s = int(a[indexa])+int(b[indexb])+carry
            carry = s//2
            ret = str(s%2)+ret
            indexa -= 1
            indexb -= 1
        while indexa>=0:
            s = int(a[indexa])+carry
            carry = s//2
            ret = str(s%2)+ret
            indexa -= 1
        while indexb>=0:
            s = int(b[indexb])+carry
            carry = s//2
            ret = str(s%2)+ret
            indexb -= 1
        if carry:
            ret = str(carry)+ret
        return ret
