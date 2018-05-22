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
class KEmptySlots:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        # li[0], li[1], li[2], ..., li[k], li[k+1]
        # min(li[1]...li[k])<li[0] and min(li[1]...li[k])<li[k+1]
        # sliding window, use a min heap to store li[1]...li[k]
        if k+2>len(flowers):
            return -1
        # li[i] stands for li[i]th day, i bloom
        li = [0]*len(flowers)
        for i in range(len(flowers)):
            li[flowers[i]-1] = i+1
        flowers = li
        minHeap = flowers[1:k+1]
        heapq.heapify(minHeap)
        removed = collections.defaultdict(int)
        start, end = 0, k+1
        ret = -1
        while end<len(flowers):
            #print(minHeap, removed)
            if not len(minHeap):
                if ret<0:
                    ret = max(flowers[start],flowers[end])
                else:
                    ret = min(ret, max(flowers[start],flowers[end]))
                start += 1
                end += 1
                continue
            while removed[minHeap[0]]:
                removed[minHeap[0]] -= 1
                heapq.heappop(minHeap)
            if flowers[start]<minHeap[0] and flowers[end]<minHeap[0]:
                if ret<0:
                    ret = max(flowers[start],flowers[end])
                else:
                    ret = min(ret, max(flowers[start],flowers[end]))
            start += 1
            removed[flowers[start]] += 1
            heapq.heappush(minHeap, flowers[end])
            end += 1
        return ret
