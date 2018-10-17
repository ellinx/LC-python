"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
"""
class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(s1, cur, n, ret):
            if n==len(cur):
                ret.append(cur)
                return
            tmp = s1[1:] if len(cur)==0 else s1
            for c in tmp:
                dfs(s1, cur+c, n, ret)

        def helper(mm, s):
            ret = ""
            for c in s:
                ret += mm[c]
            return ret[::-1]

        mm = {"0":"0","1":"1","6":"9","8":"8","9":"6"}
        s1 = "01689"
        s2 = "180"
        p1 = []
        dfs(s1, "", n//2, p1)
        if n%2==0:
            return [each+helper(mm,each) for each in p1]
        ret = []
        for c in s2:
            ret += [each+c+helper(mm,each) for each in p1]
        return ret
