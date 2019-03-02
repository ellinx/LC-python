"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
1. You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
2. Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        pq = []
        for num in counter:
            heapq.heappush(pq, [counter[num], num])
            if len(pq)>k:
                heapq.heappop(pq)
        ret = []
        while len(pq):
            ret.append(heapq.heappop(pq)[1])
        return ret[::-1]
