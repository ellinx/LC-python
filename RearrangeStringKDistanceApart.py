import heapq, collections
"""
Given a non-empty string s and an integer k,
rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters.
If it is not possible to rearrange the string, return an empty string "".

Example 1:
Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least distance 3 from each other.

Example 2:
Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.

Example 3:
Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.
"""
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k<=1:
            return s
        counter = collections.Counter(s)
        q = collections.deque([None]*k)
        pq = [[-counter[k],k] for k in counter]
        heapq.heapify(pq)
        ret = []
        while len(pq)>0 or q[0] is not None:
            cur = q.popleft()
            if cur is not None:
                heapq.heappush(pq, cur)
            num, c = heapq.heappop(pq)
            ret.append(c)
            num += 1
            if num<0:
                q.append([num,c])
            else:
                q.append(None)
            #print(ret,q)
        if len(ret)==len(s):
            return "".join(ret)
        return ""
