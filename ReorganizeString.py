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
class ReorganizeString:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # select character with most frequency, maxHeap
        # after each character is selected, put it in a queue with size 1 (1 position apart)
        counter = collections.Counter(S)
        maxHeap = [(-counter[k], k) for k in counter]
        heapq.heapify(maxHeap)
        q = collections.deque()
        ret = ''
        while len(maxHeap):
            cur = heapq.heappop(maxHeap)
            ret += cur[1]
            if len(q):
                temp = q.popleft()
                if temp[0]!=0:
                    heapq.heappush(maxHeap,temp)
            q.append((cur[0]+1, cur[1]))
        if len(q) and q[0][0]!=0:
            return ''
        return ret
