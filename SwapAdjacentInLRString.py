"""
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL",
a move consists of either replacing one occurrence of "XL" with "LX",
or replacing one occurrence of "RX" with "XR".

Given the starting string start and the ending string end,
return True if and only if there exists a sequence of moves to transform one string to the other.

Example:
Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True

Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

Note:
1. 1 <= len(start) = len(end) <= 10000.
2. Both start and end will only consist of characters in {'L', 'R', 'X'}.
"""
class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start)!=len(end):
            return False
        i1, i2 = 0, 0
        while i1<len(start) and i2<len(end):
            while i1<len(start) and start[i1]=='X':
                i1 += 1
            while i2<len(end) and end[i2]=="X":
                i2 += 1
            if i1==len(start) and i2==len(end):
                return True
            if i1==len(start) or i2==len(end):
                return False
            if start[i1]!=end[i2]:
                return False
            if start[i1]=='L' and i1<i2:
                return False
            if start[i1]=='R' and i1>i2:
                return False
            i1 += 1
            i2 += 1
        return True
