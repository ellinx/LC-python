"""
 A string S of lowercase letters is given.
 We want to partition this string into as many parts as possible so that each letter appears in at most one part,
 and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

1. S will have length in range [1, 500].
2. S will consist of lowercase letters ('a' to 'z') only.

"""
class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = dict()
        for i in range(len(S)):
            last[S[i]] = i
        start, cur, end = 0, 0 ,last[S[0]]
        ret = []
        while cur<=end:
            end = max(end, last[S[cur]])
            if cur==end:
                ret.append(end-start+1)
                if cur+1<len(S):
                    start, cur, end = end+1, end+1 ,last[S[end+1]]
                    continue
                break
            cur += 1
        return ret
