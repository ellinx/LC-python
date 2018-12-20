"""

Given an integer array A, and an integer target,
return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.


Example 1:

Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:

Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.


Note:

3 <= A.length <= 3000
0 <= A[i] <= 100
0 <= target <= 300
"""
class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9+7
        counter = collections.Counter(A)
        A.sort()
        ret = 0
        for i in range(len(A)-2):
            if A[i]+A[i+1]+A[i+2]>target:
                break
            if (i>0 and A[i-1]==A[i]) or A[i]+A[-2]+A[-1]<target:
                continue
            j, k = i+1, len(A)-1
            while j<k:
                #print(A[i],A[j],A[k],ret)
                if A[i]+A[j]+A[k]==target:
                    ci, cj, ck = counter[A[i]], counter[A[j]], counter[A[k]]
                    if A[i]!=A[j] and A[j]!=A[k]:
                        ret += (ci * cj * ck) % MOD
                    elif A[i]==A[j] and A[j]!=A[k]:
                        ret += (ci * (ci - 1) // 2 * ck) % MOD
                    elif A[i]!=A[j] and A[j]==A[k]:
                        ret += (ci * cj * (cj - 1) // 2) % MOD
                    else:
                        ret += (ci * (ci - 1)*(ci - 2) // 6) % MOD
                    j += 1
                    k -= 1
                    while j-1>=0 and j<k and A[j-1]==A[j]:
                        j += 1
                    while k+1<len(A) and k>j and A[k]==A[k+1]:
                        k -= 1
                elif A[i]+A[j]+A[k]<target:
                    j += 1
                else:
                    k -= 1
        return ret % MOD
