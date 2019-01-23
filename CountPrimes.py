"""
Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 0
        dp = [True]*n
        count = 0
        for i in range(2,n):
            if not dp[i]:
                continue
            count += 1
            j = i
            while j*i<n:
                dp[j*i] = False
                j += 1
        return count
