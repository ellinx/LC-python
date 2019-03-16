"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
1. If there is no such window in S that covers all characters in T, return the empty string "".
2. If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.Counter(t)
        total = len(t)
        ret = ""
        l, r = 0, 0
        while r<len(s):
            # print(l,r)
            if s[r] not in counter:
                r += 1
                continue
            if counter[s[r]]>0:
                total -= 1
            counter[s[r]] -= 1
            r += 1
            while total==0:
                if ret=="" or len(ret)>r-l:
                    ret = s[l:r]
                if s[l] not in counter:
                    l += 1
                    continue
                if counter[s[l]]>=0:
                    total += 1
                counter[s[l]] += 1
                l += 1
        return ret
