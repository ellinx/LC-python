"""
Given an array of integers A, find the sum of min(B),
where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:
Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.


Note:

1. 1 <= A.length <= 30000
2. 1 <= A[i] <= 30000
"""
class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mod = 10**9+7
        n = len(A)
        left, right = [0]*n, [0]*n
        stk = collections.deque()
        for i,a in enumerate(A):
            count = 1
            while len(stk) and stk[-1][0]>=a:
                count += stk.pop()[1]
            left[i] = count
            stk.append([a, count])
        stk = collections.deque()
        for i in range(n-1,-1,-1):
            count = 1
            a = A[i]
            while len(stk) and stk[-1][0]>a:
                count += stk.pop()[1]
            right[i] = count
            stk.append([a, count])
        ret = 0
        for i in range(n):
            ret += (A[i]*left[i]*right[i])%mod
        return ret%mod
