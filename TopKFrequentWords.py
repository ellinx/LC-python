"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
1. You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
2. Input words contain only lowercase letters.

Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        pq = []
        for word in counter:
            heapq.heappush(pq, [counter[word], word])
            if len(pq)>k:
                items = [heapq.heappop(pq)]
                while len(pq)>0 and pq[0][0]==items[-1][0]:
                    items.append(heapq.heappop(pq))
                items.pop()
                for each in items:
                    heapq.heappush(pq, each)
        pq.sort(key=lambda x:[-x[0],x[1]])
        return [each[1] for each in pq]
