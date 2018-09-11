"""
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:
Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3

Example 2:
Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4

Example 3:
Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

Note: 1 <= N <= 10 ^ 9.
"""
class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        ret = 0
        for i in range(N):
            # calculate sum of k, k+1, ..., k+i
            # k*(i+1)+i*(i+1)/2 = N
            tmp = N-i*(i+1)//2
            if tmp<=0:
                break
            if tmp%(i+1)==0:
                #print(tmp//(i+1), i)
                ret += 1
        return ret
