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
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, end = 0, 0
        ret = 0
        counter = dict()
        while end<len(s):
            if s[end] not in counter:
                counter[s[end]] = 0
            counter[s[end]] += 1
            while len(counter)>2:
                if counter[s[start]]==1:
                    counter.pop(s[start])
                else:
                    counter[s[start]] -= 1
                start += 1
            ret = max(ret, end-start+1)
            end += 1
        return ret
