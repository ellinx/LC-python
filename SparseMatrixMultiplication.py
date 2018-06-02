"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""
class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = [[0]*len(B[0]) for _ in range(len(A))]
        for j in range(len(ret[0])):
            for k in range(len(A[0])):
                if B[k][j]:
                    for i in range(len(ret)):
                        ret[i][j] += A[i][k]*B[k][j]
        return ret

    # def multiply(self, A, B):
    #     """
    #     :type A: List[List[int]]
    #     :type B: List[List[int]]
    #     :rtype: List[List[int]]
    #     """
    #     ret = [[0]*len(B[0]) for _ in range(len(A))]
    #     for j in range(len(ret[0])):
    #         for i in range(len(ret)):
    #             for k in range(len(A[i])):
    #                 ret[i][j] += A[i][k]*B[k][j]
    #     return ret
