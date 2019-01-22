"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x>=0 else -1
        if x<0:
            x = -x
        ret = sign*int(str(x)[::-1])
        if ret>2**31-1 or ret<-2**31:
            return 0
        return ret

class Solution2:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            ret = self.reverse(-x)
            if ret>2**31:
                return 0
            return -ret
        stk = collections.deque()
        while x>0:
            stk.append(x%10)
            x //= 10
        ret = 0
        while len(stk)>0:
            ret = ret*10+stk.popleft()
        if ret>2**31-1:
            return 0
        return ret
