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
        counter = dict()
        ret = 0
        start, end = 0, 0
        while end<len(s):
            counter[s[end]] = counter.get(s[end], 0)+1
            while len(counter)>2:
                counter[s[start]] -= 1
                if counter[s[start]]==0:
                    counter.pop(s[start])
                start += 1
            ret = max(ret, end-start+1)
            end += 1
        return ret
