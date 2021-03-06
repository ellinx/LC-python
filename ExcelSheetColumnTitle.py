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
        ret = ""
        while n>26:
            remain = n%26
            n //= 26
            if remain==0:
                remain = 26
                n -=1
            ret = chr(ord('A')+remain-1)+ret
        return chr(ord('A')+n-1)+ret

class Solution2:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        title = "#ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ret = ""
        if n%26==0:
            if n==26:
                return 'Z'
            return self.convertToTitle((n-26)//26)+'Z'
        if n>26:
            return self.convertToTitle(n//26)+title[(n%26)]
        return title[n]
