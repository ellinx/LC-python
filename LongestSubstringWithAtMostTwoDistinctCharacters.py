"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.


"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = {}
        l, r = 0, 0
        ret = 0
        while r<len(s):
            if s[r] in counter:
                counter[s[r]] += 1
                r += 1
                ret = max(ret, r-l)
                continue
            counter[s[r]] = 1
            r += 1
            while len(counter)>2:
                counter[s[l]] -= 1
                if counter[s[l]]==0:
                    counter.pop(s[l])
                l += 1
            ret = max(ret, r-l)
        return ret
