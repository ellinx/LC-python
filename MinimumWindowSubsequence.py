"""

Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "".
If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input:
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation:
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.


Note:

1. All the strings in the input will only contain lowercase letters.
2. The length of S will be in the range [1, 20000].
3. The length of T will be in the range [1, 100].
"""
class Solution:
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        def dfs(S, s1, T, s2, mm):
            if s2==len(T):
                return s1-1
            if mm[s2]==-1:
                return -1
            if s1<=mm[s2]:
                return mm[-1]
            for i in range(s1,len(S)):
                if T[s2]==S[i]:
                    mm[s2] = i
                    return dfs(S, i+1, T, s2+1, mm)
            mm[s2] = -1
            return -1

        ret = ""
        mm = [0]*len(T)
        for i in range(len(S)-len(T)+1):
            #print(mm)
            if S[i]==T[0]:
                mm[0] = i
                tmp = dfs(S, i+1, T, 1, mm)
                if tmp==-1:
                    break
                if len(ret)==0 or len(ret)>tmp-i+1:
                    ret = S[i:tmp+1]
            if len(ret)==len(T):
                break
        return ret
