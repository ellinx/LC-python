"""
Let's call an array A a mountain if the following properties hold:

1. A.length >= 3
2. There exists some 0 < i < A.length - 1 such that
    A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]

Given an array that is definitely a mountain, return any i such that
A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:
Input: [0,1,0]
Output: 1

Example 2:
Input: [0,2,1,0]
Output: 1

Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
"""
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l, r = 0, len(A)-1
        while l<r:
            m = l+(r-l)//2
            if A[m]<A[m+1]:
                l = m+1
            else:
                r = m
        return l
