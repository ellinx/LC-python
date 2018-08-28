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
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x, -n)
        mm = []
        bits = []
        val, pos = x, 0
        while (n>>pos)>0:
            mm.append(val)
            if ((n>>pos)&1)==1:
                bits.append(pos)
            pos += 1
            val *= val
        #print(mm, bits)
        ret = 1.0
        for each in bits:
            ret *= mm[each]
        return ret
