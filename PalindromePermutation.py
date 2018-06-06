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
        count = collections.Counter(s)
        if len(s)%2==0:
            for k in count:
                if count[k]%2!=0:
                    return False
            return True
        odd = 0
        for k in count:
            if count[k]%2!=0:
                odd += 1
            if odd>1:
                break
        return odd==1
