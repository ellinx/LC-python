"""
Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?
"""
class Solution:
    # recursive
    def isPowerOfThree(self, n: 'int') -> 'bool':
        if n<1:
            return False
        if n==1:
            return True
        if n%3!=0:
            return False
        return self.isPowerOfThree(n//3)


class Solution2:
    # iterative
    def isPowerOfThree(self, n: 'int') -> 'bool':
        if n<1:
            return False
        while n>=3:
            if n%3!=0:
                return False
            n //= 3
        return n==1
