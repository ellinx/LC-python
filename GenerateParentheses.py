"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(l, r, cur, ret):
            if l==0 and r==0:
                ret.append(cur)
                return
            if l:
                dfs(l-1,r,cur+"(", ret)
            if r and r>l:
                dfs(l,r-1,cur+")",ret)

        ret = []
        dfs(n,n,"",ret)
        return ret
