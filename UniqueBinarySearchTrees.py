"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n, mm):
            if n<=1:
                return 1
            if n in mm:
                return mm[n]
            ret = 0
            for i in range(1,n+1):
                ret += helper(i-1, mm)*helper(n-i, mm)
            mm[n] = ret
            return ret

        return helper(n, dict())
