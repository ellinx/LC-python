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
        count = collections.Counter(t)
        total = len(t)
        ret = ""
        start, end = 0, 0
        while end<len(s):
            if s[end] not in count:
                end += 1
                continue
            if count[s[end]]>0:
                total -= 1
            count[s[end]] -= 1
            #print(count, total)
            while total==0:
                if ret=="":
                    ret = s[start:end+1]
                else:
                    ret = s[start:end+1] if end-start+1<len(ret) else ret
                # remove start
                #print(start,end)
                if s[start] in count:
                    if count[s[start]]>=0:
                        total += 1
                    count[s[start]] += 1
                start += 1
            end += 1
        return ret
