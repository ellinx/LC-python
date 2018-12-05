"""
 Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ret = 0
        counter = dict()
        l, r = 0, 0
        while r<len(s):
            counter[s[r]] = counter.get(s[r], 0)+1
            r += 1
            while len(counter)>k:
                counter[s[l]] -= 1
                if counter[s[l]]==0:
                    counter.pop(s[l])
                l += 1
            ret = max(ret, r-l)
        return ret
