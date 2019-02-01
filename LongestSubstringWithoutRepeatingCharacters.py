"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.

Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        counter = collections.defaultdict(int)
        l, r = 0, 0
        while r<len(s):
            counter[s[r]] += 1
            while counter[s[r]]>1:
                counter[s[l]] -= 1
                l += 1
            r += 1
            ret = max(ret, r-l)
        return ret
