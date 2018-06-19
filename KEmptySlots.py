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
        if k+2>N:
            return -1
        # bloomDay[i] is ith position will bloom on day bloomDay[i]
        bloomDay = [0]*(N+1)
        for i in range(N):
            bloomDay[flowers[i]] = i+1
        #print(bloomDay)
        minHeap = [(bloomDay[i],i) for i in range(2,k+2)]
        heapq.heapify(minHeap)
        start, end = 1, k+2
        ret = -1
        if k==0:
            while end<N+1:
                if ret==-1:
                    ret = max(bloomDay[start],bloomDay[end])
                else:
                    ret = min(ret, max(bloomDay[start],bloomDay[end]))
                start += 1
                end += 1
            return ret
        while True:
            while minHeap[0][1]<=start:
                heapq.heappop(minHeap)
            #print(start,end,minHeap)
            if minHeap[0][0]>bloomDay[start] and minHeap[0][0]>bloomDay[end]:
                if ret==-1:
                    ret = max(bloomDay[start],bloomDay[end])
                else:
                    ret = min(ret, max(bloomDay[start],bloomDay[end]))
            if end+1==N+1:
                break
            heapq.heappush(minHeap,(bloomDay[end],end))
            start += 1
            end += 1
        return ret
