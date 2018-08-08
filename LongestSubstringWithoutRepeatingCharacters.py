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
        counter = collections.defaultdict(int)
        ret = 0
        start, end = 0, 0
        while end<len(s):
            counter[s[end]] += 1
            if counter[s[end]]==1:
                end += 1
                ret = max(ret, end-start)
                continue
            while counter[s[end]]==2:
                counter[s[start]] -= 1
                start += 1
            end += 1
        return ret
