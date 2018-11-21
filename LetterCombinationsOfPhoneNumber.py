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
        if len(digits)==0:
            return []
        mapping = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        cur = [""]
        for digit in digits:
            nxt = []
            for c in mapping[int(digit)]:
                for s in cur:
                    nxt.append(s+c)
            cur = nxt
        return cur
