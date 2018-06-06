"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...

Example 1:
Input: 1
Output: "A"

Example 2:
Input: 28
Output: "AB"

Example 3:
Input: 701
Output: "ZY"


"""
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        def helper(n):
            numMap = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
            ret = ""
            if n==0:
                return ret
            while n:
                if n%26==0:
                    return helper(n//26-1)+"Z"+ret
                ret = numMap[(n%26)] + ret
                n //= 26
            return ret
        return helper(n)
