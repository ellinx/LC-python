"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:

    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.


"""
class Solution:
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
                if counter[s[end]]>0:
                    total -= 1
                counter[s[end]] -= 1
            end += 1
            while total==0:
                if len(ret)==0 or len(ret)>end-start:
                    ret = s[start:end]
                if s[start] in counter:
                    if counter[s[start]]>=0:
                        total += 1
                    counter[s[start]] += 1
                start += 1
        return ret
