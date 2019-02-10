"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.

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
class Solution:
    def kthSmallest(self, matrix: 'List[List[int]]', k: 'int') -> 'int':
        pq = []
        n = len(matrix)
        for i in range(n):
            heapq.heappush(pq, [matrix[0][i], 0, i])
        while k>1:
            cur,i,j = heapq.heappop(pq)
            k -= 1
            if i+1<n:
                heapq.heappush(pq, [matrix[i+1][j],i+1,j])
        return pq[0][0]

class Solution2:
    def kthSmallest(self, matrix: 'List[List[int]]', k: 'int') -> 'int':
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n-1][n-1]
        while left<right:
            mid = left+(right-left)//2
            rank, j = 0, n-1
            for i in range(n):
                while j>=0 and matrix[i][j]>mid:
                    j -= 1
                rank += j+1
            if rank<k:
                left = mid+1
                # mid definately won't be the answer
            else:
                # mid may be the answer, will narrow down range
                right = mid
        return left
