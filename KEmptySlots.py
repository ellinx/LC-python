"""
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days.
In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N.
Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming,
and also the number of flowers between them is k and these flowers are not blooming.

If there isn't such day, output -1.

Example 1:
Input:
flowers: [1,3,2]
k: 1
Output: 2
Explanation: In the second day, the first and the third flower have become blooming.

Example 2:
Input:
flowers: [1,2,3]
k: 1
Output: -1

Note:
The given array will be in the range [1, 20000].
"""
class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        N = len(flowers)
        bloomDay = [-1]*(N+1)
        for day in range(N):
            bloomDay[flowers[day]] = day+1
        #print(bloomDay)
        ret = float('inf')
        minQ = collections.deque()
        l, r = 1, 3
        while r<N+1:
            while len(minQ) and bloomDay[minQ[-1]]>bloomDay[r-1]:
                minQ.pop()
            minQ.append(r-1)
            if r-l-1>k:
                l += 1
            while len(minQ) and minQ[0]<=l:
                minQ.popleft()
            if r-l-1==k:
                if (k==0 and len(minQ)==0) or bloomDay[minQ[0]]>max(bloomDay[l],bloomDay[r]):
                    #print(l,r, pq)
                    ret = min(ret, max(bloomDay[l],bloomDay[r]))
            r += 1
        if ret==float('inf'):
            return -1
        return ret


class Solution2:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        def insertIndex(blooms, target):
            l, r = 0, len(blooms)-1
            while l<=r:
                m = l+(r-l)//2
                if blooms[m]>target:
                    r = m-1
                else:
                    l = m+1
            return l

        N = len(flowers)
        blooms = []
        for i,x in enumerate(flowers):
            idx = insertIndex(blooms, x)
            blooms.insert(idx, x)
            #print(i, blooms)
            if idx-1>=0 and blooms[idx]-blooms[idx-1]-1==k:
                return i+1
            if idx+1<len(blooms) and blooms[idx+1]-blooms[idx]-1==k:
                return i+1
        return -1
