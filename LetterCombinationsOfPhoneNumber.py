"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class LetterCombinationsOfPhoneNumber:
    # use dfs
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not len(digits):
            return []
        li = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        def dfs(li, digits, cur, ret):
            if not len(digits):
                ret.append(cur)
                return
            for c in li[int(digits[0])]:
                dfs(li, digits[1:], cur+c, ret)
        ret = []
        dfs(li, digits, "", ret)
        return ret
