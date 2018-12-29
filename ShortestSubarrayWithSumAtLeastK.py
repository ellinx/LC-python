"""
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.


Example 1:

Input: A = [1], K = 1
Output: 1

Example 2:

Input: A = [1,2], K = 4
Output: -1

Example 3:

Input: A = [2,-1,2], K = 3
Output: 3



Note:

1. 1 <= A.length <= 50000
2. -10 ^ 5 <= A[i] <= 10 ^ 5
3. 1 <= K <= 10 ^ 9


"""
class Solution:
    """
    Time: O(n) where n is length of A
    Space: O(n)
    """
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        total = 0
        ret = -1
        dq = collections.deque()
        dq.append([0,-1])
        for i,a in enumerate(A):
            total += a
            while len(dq) and total-dq[0][0]>=K:
                ret = i-dq[0][1] if ret==-1 else min(ret, i-dq[0][1])
                dq.popleft()
            while len(dq) and dq[-1][0]>total:
                dq.pop()
            dq.append([total, i])
        return ret
