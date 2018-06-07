"""
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:
Input: "aabb"
Output: ["abba", "baab"]

Example 2:
Input: "abc"
Output: []

"""
class Solution:
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # DFS generate all strs
        def dfs(s, used, cur, ret):
            if len(cur)==len(s):
                ret.append(cur)
                return
            pre = None
            for i in range(len(s)):
                if not used[i] and pre!=s[i]:
                    used[i] = True
                    dfs(s, used, cur+s[i], ret)
                    pre = s[i]
                    used[i] = False


        counter = collections.Counter(s)
        ret = []
        part1 = ""
        if len(s)%2==0:
            for k in counter:
                if counter[k]%2==1:
                    return []
                part1 += k*(counter[k]//2)
            used = [False]*len(part1)
            dfs(sorted(part1), used, "", ret)
            for i in range(len(ret)):
                ret[i] = ret[i]+ret[i][::-1]
        else:
            mid = ""
            for k in counter:
                if counter[k]%2==1:
                    if mid!="":
                        return []
                    mid = k
                part1 += k*(counter[k]//2)
            used = [False]*len(part1)
            dfs(sorted(part1), used, "", ret)
            for i in range(len(ret)):
                ret[i] = ret[i]+mid+ret[i][::-1]
        return ret
