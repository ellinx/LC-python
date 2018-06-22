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
        counter = dict()
        start, end = 0, 0
        ret = 0
        while end<len(s):
            if s[end] not in counter:
                counter[s[end]] = 0
            counter[s[end]] += 1
            while len(counter)>k:
                if counter[s[start]]==1:
                    counter.pop(s[start])
                else:
                    counter[s[start]] -= 1
                start += 1
            ret = max(ret, end-start+1)
            end += 1
        return ret
