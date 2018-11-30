"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        def helper(s1, i1, s2, i2, s3, i3, mm):
            key = str(i1)+":"+str(i2)+":"+str(i3)
            if key in mm:
                return mm[key]
            if i1==len(s1):
                return s2[i2:]==s3[i3:]
            if i2==len(s2):
                return s1[i1:]==s3[i3:]
            if s1[i1]==s3[i3]:
                if helper(s1, i1+1, s2, i2, s3, i3+1, mm):
                    mm[key] = True
                    return True
            if s2[i2]==s3[i3]:
                if helper(s1, i1, s2, i2+1, s3, i3+1, mm):
                    mm[key] = True
                    return True
            mm[key] = False
            return False

        if len(s1)+len(s2)!=len(s3):
            return False
        return helper(s1, 0, s2, 0, s3, 0, dict())
