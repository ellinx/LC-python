"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

"""
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.Counter(s)
        odd = False
        ret = 0
        for k in counter:
            if counter[k]%2==1:
                odd = True
            ret += counter[k]//2
        ret *= 2
        if odd:
            ret += 1
        return ret
