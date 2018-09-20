"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution:
    # use dfs
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(digits, start, cur, ret):
            if start == len(digits):
                ret.append(cur)
                return
            mm = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
            for c in mm[int(digits[start])]:
                dfs(digits, start+1, cur+c, ret)

        ret = []
        if len(digits) == 0:
            return []
        dfs(digits, 0, "", ret)
        return ret

class Solution2:
    # BFS
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        strs = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        ret = []
        for a in digits:
            if len(ret)==0:
                ret = list(strs[int(a)])
                continue
            ret = [ sub+c for sub in ret for c in strs[int(a)]]
        return ret
