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
        def helper(x, n, mm):
            if n in mm:
                return mm[n]
            n1 = n//2
            n2 = n-n1
            mm[n] = helper(x, n1, mm)*helper(x, n2, mm)
            return mm[n]

        if x==0:
            return 0
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x, -n)
        mm = dict()
        mm[0], mm[1] = 1, x
        return helper(x, n, mm)


class Solution2:
    def myPow(self, x: float, n: int) -> float:
        def biSearch(mm,n):
            l, r = 0, len(mm)-1
            while l<=r:
                mid = l+(r-l)//2
                if 2**mid<=n:
                    if mid+1>r or 2**(mid+1)>n:
                        return mid
                    l = mid+1
                else:
                    r = mid-1
            return l

        if n<0:
            return 1/self.myPow(x,-n)
        mm = [x]
        ret = 1
        while n>0:
            while n>2**(len(mm)-1):
                mm.append(mm[-1]*mm[-1])
            idx = biSearch(mm,n)
            ret *= mm[idx]
            n -= 2**idx
        return ret
