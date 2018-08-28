import collections, heapq
"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"

Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""
class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter = collections.Counter(S)
        pq = [[-counter[k], k] for k in counter]
        heapq.heapify(pq)
        rest = None
        ret = ""
        while len(pq):
            cur = heapq.heappop(pq)
            ret += cur[1]
            cur[0] += 1
            if rest is not None and rest[0]!=0:
                heapq.heappush(pq, rest)
            rest = cur
        if rest is not None and rest[0]!=0:
            return ""
        return ret
