"""
You have k lists of sorted integers in ascending order.
Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Note:
1. The given list may contain duplicates, so ascending order means >= here.
2. 1 <= k <= 3500
3. -10^5 <= value of elements <= 10^5.
"""
class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pq = []
        mx = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(pq, [nums[i][0], i, 0])
            mx = max(mx, nums[i][0])
        ret = [pq[0][0], mx]
        while len(pq)==len(nums):
            if ret[1]-ret[0]>mx-pq[0][0]:
                ret = [pq[0][0], mx]
            cur = heapq.heappop(pq)
            if cur[2]+1<len(nums[cur[1]]):
                heapq.heappush(pq, [nums[cur[1]][cur[2]+1], cur[1], cur[2]+1])
                mx = max(mx, nums[cur[1]][cur[2]+1])
        return ret
