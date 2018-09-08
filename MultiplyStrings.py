"""
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Note:

1. The length of both num1 and num2 is < 110.
2. Both num1 and num2 contain only digits 0-9.
3. Both num1 and num2 do not contain any leading zero, except the number 0 itself.
4. You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def multiply_str(num, digit):
            ret = ""
            carry = 0
            for c in reversed(num):
                tmp = int(c)*int(digit)+carry
                tmp, carry = tmp%10, tmp//10
                ret = str(tmp)+ret
            if carry>0:
                ret = str(carry)+ret
            return ret

        def add_str(num1, num2):
            ret = ""
            i1, i2 = len(num1)-1, len(num2)-1
            carry = 0
            while i1>=0 and i2>=0:
                tmp = int(num1[i1])+int(num2[i2])+carry
                tmp, carry = tmp%10, tmp//10
                ret = str(tmp)+ret
                i1 -= 1
                i2 -= 1
            while i1>=0:
                tmp = int(num1[i1])+carry
                tmp, carry = tmp%10, tmp//10
                ret = str(tmp)+ret
                i1 -= 1
            while i2>=0:
                tmp = int(num2[i2])+carry
                tmp, carry = tmp%10, tmp//10
                ret = str(tmp)+ret
                i2 -= 1
            if carry>0:
                ret = str(carry)+ret
            return ret

        if num1=='0' or num2=='0':
            return '0'
        ret = "0"
        for i in range(len(num2)-1,-1,-1):
            tmp = multiply_str(num1, num2[i])
            tmp += '0'*(len(num2)-1-i)
            ret = add_str(ret, tmp)
        return ret
