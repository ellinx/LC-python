"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n!=1 and n not in visited:
            visited.add(n)
            nxt = 0
            for c in str(n):
                nxt += int(c)**2
            n = nxt
        if n==1:
            return True
        return False

class Solution2:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def getNext(n):
            ret = 0
            for c in str(n):
                ret += int(c)**2
            return ret

        fast, slow = n, n
        while True:
            slow = getNext(slow)
            fast = getNext(fast)
            fast = getNext(fast)
            if fast==slow:
                break
        return fast==1

# test
if __name__ == "__main__":
    tmp = Solution()
    result = tmp.isHappy(19)
    print(result)
