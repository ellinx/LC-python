"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        def dfs(s, mm):
            if s in mm:
                return mm[s]
            ret = len(s)-1
            for end in range(len(s)-1, -1, -1):
                l, r = 0, end
                while l<r:
                    if s[l]==s[r]:
                        l += 1
                        r -= 1
                        continue
                    break
                if l>=r:
                    if end+1==len(s):
                        return 0
                    ret = min(ret, 1+dfs(s[end+1:], mm))
            mm[s] = ret
            return ret

        return dfs(s, dict())
