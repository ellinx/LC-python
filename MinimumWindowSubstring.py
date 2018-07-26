"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:

    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.


"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = collections.Counter(t)
        total = len(t)
        ret = ""
        start, end = 0, 0
        while end<len(s):
            if s[end] in counter:
                counter[s[end]] -= 1
                if counter[s[end]]>=0:
                    total -= 1
            while total==0:
                if ret=="" or len(ret)>end-start+1:
                    ret = s[start:end+1]
                if s[start] in counter:
                    counter[s[start]] += 1
                    if counter[s[start]]>0:
                        total += 1
                start += 1
            end += 1
        return ret
