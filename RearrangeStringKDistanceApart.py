import heapq, collections
"""

"""
class Solution:
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k<=1:
            return s
        q = collections.deque()
        counter = collections.Counter(s)
        maxHeap = [(-counter[k], k) for k in counter]
        heapq.heapify(maxHeap)
        ret = ""
        while len(maxHeap):
            cur = heapq.heappop(maxHeap)
            ret += cur[1]
            q.append((cur[0]+1,cur[1]))
            if len(q)==k:
                temp = q.popleft()
                if temp[0]!=0:
                    heapq.heappush(maxHeap, temp)
        for each in q:
            if each[0]!=0:
                return ""
        return ret
