"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
"""
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x==0 or x==1:
            return x
        if x==-1:
            return 1 if n%2==0 else -1
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x,-n)
        bitVal = [0]*32
        bitVal[0] = x
        for i in range(1,32):
            bitVal[i] = bitVal[i-1]*bitVal[i-1]
        #print(bitVal)
        bitset = set()
        for i in range(32):
            if (n&(1<<i))!=0:
                bitset.add(i)
        #print(bitset)
        ret = 1
        for bit in bitset:
            ret *= bitVal[bit]
        return ret
