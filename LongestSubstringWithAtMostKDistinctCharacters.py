"""
 Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l, r = 0, 0
        counter = collections.defaultdict(int)
        total = 0
        ret = 0
        while r<len(s):
            if counter[s[r]]==0:
                total += 1
            counter[s[r]] += 1
            r += 1
            while total>k:
                if counter[s[l]]==1:
                    total -= 1
                counter[s[l]] -= 1
                l += 1
            ret = max(ret, r-l)
        return ret
