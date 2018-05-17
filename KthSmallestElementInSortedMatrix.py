"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n^2.
"""

class KthSmallestElementInSortedMatrix:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        minHeap = [(matrix[0][i],0,i) for i in range(n)]
        heapq.heapify(minHeap)
        for i in range(k-1):
            cur = heapq.heappop(minHeap)
            if cur[1]==n-1:
                continue
            heapq.heappush(minHeap, (matrix[cur[1]+1][cur[2]], cur[1]+1, cur[2]))
        return heapq.heappop(minHeap)[0]
