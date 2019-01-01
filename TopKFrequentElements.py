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
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += 1
        pq = []
        for key in counter:
            heapq.heappush(pq, [-counter[key], key])
        ret = []
        while len(ret)<k and len(pq):
            ret.append(heapq.heappop(pq)[1])
        return ret
