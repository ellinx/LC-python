"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:
Input: "code"
Output: false

Example 2:
Input: "aab"
Output: true

Example 3:
Input: "carerac"
Output: true

"""
class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counter = collections.Counter(s)
        odd = 0
        for k in counter:
            if counter[k]%2==0:
                continue
            if odd>0:
                return False
            odd += 1
        return True
