"""
Two images A and B are given, represented as binary, square matrices of the same size.
(A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units),
and place it on top of the other image.
After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.

Notes:
1. 1 <= A.length = A[0].length = B.length = B[0].length <= 30
2. 0 <= A[i][j], B[i][j] <= 1
"""
class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        pA, pB = [], []
        for i in range(m):
            for j in range(n):
                if A[i][j]==1:
                    pA.append((i,j))
                if B[i][j]==1:
                    pB.append((i,j))
        ret = 0
        mm = collections.defaultdict(int)
        for ai, aj in pA:
            for bi, bj in pB:
                key = (bi-ai, bj-aj)
                mm[key] += 1
                ret = max(ret, mm[key])
        return ret
