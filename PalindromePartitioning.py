"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(s):
            return s==s[::-1]

        def dfs(s, start, cur, ret):
            if start==len(s):
                ret.append(cur)
                return
            for i in range(start, len(s)):
                if isPalindrome(s[start:i+1]):
                    dfs(s, i+1, cur+[s[start:i+1]], ret)

        ret = []
        dfs(s, 0, [], ret)
        return ret
