"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]


"""
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s, start, cur, ret):
            if start==len(s):
                if len(cur)==4:
                    ret.append(".".join(cur))
                return
            # no leading zero
            if s[start]=="0":
                dfs(s, start+1, cur+["0"], ret)
                return
            for i in range(1,4):
                if start+i>len(s):
                    break
                if int(s[start:start+i])>255:
                    break
                dfs(s, start+i, cur+[s[start:start+i]], ret)

        ret = []
        if len(s)>12 or len(s)<4:
            return ret
        dfs(s, 0, [], ret)
        return ret
