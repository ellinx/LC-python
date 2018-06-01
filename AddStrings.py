"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        index1, index2 = len(num1)-1, len(num2)-1
        ret = ''
        while index1>=0 and index2>=0:
            s = int(num1[index1])+int(num2[index2])+carry
            carry = s//10
            ret = str(s%10)+ret
            index1 -= 1
            index2 -= 1
        while index1>=0:
            s = int(num1[index1])+carry
            carry = s//10
            ret = str(s%10)+ret
            index1 -= 1
        while index2>=0:
            s = int(num2[index2])+carry
            carry = s//10
            ret = str(s%10)+ret
            index2 -= 1
        if carry:
            ret = str(carry)+ret
        return ret
