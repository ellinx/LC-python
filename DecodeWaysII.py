"""
A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".

Example 2:
Input: "1*"
Output: 9 + 9 = 18

Note:
1. The length of the input string will fit in range [1, 105].
2. The input string will only contain the character '*' and digits '0' - '9'.
"""
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        MOD = 10**9+7
        if N==0:
            return 0
        a = 1
        if s[0]=='0':
            b = 0
        elif s[0]=='*':
            b = 9
        else:
            b = 1
        for i in range(1,N):
            c = 0
            if s[i]=='*':
                c += b*9
            elif int(s[i])>=1 and int(s[i])<=9:
                c += b
            if i-1>=0:
                digits = s[i-1:i+1]
                if digits=='**':
                    c += a*(9+6)
                elif digits[0]=='*':
                    if int(digits[1])>=0 and int(digits[1])<=6:
                        c += a*2
                    else:
                        c += a
                elif digits[1]=='*':
                    if digits[0]=='1':
                        c += a*9
                    elif digits[0]=='2':
                        c += a*6
                else:
                    if int(digits)>=10 and int(digits)<=26:
                        c += a
            c %= MOD
            a, b = b, c
        return b
