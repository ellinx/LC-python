"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
class Solution:
    # DFS
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(mp, digits, start, cur, ret):
            if start==len(digits):
                if len(cur)>0:
                    ret.append("".join(cur))
                return
            for c in mp[int(digits[start])]:
                dfs(mp, digits, start+1, cur+[c], ret)

        mp = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        ret = []
        dfs(mp, digits, 0, [], ret)
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
