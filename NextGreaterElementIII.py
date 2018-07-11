"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer
which has exactly the same digits existing in the integer n and is greater in value than n.
If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21



Example 2:

Input: 21
Output: -1

"""
class Solution:
    """
    Thoughts:
    1. similar idea of next permutation
    """
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        start = len(s)-2
        while start>=0:
            if int(s[start])<int(s[start+1]):
                break
            start -= 1
        if start<0:
            return -1
        index = start+1
        for i in range(start+1,len(s)):
            if int(s[i])>int(s[start]) and int(s[i])<int(s[index]):
                index = i
        ret = int(s[:start]+s[index]+"".join(sorted([s[j] for j in range(start+1,len(s)) if j!=index]+[s[start]])))
        if ret<2**31-1:
            return ret
        return -1
