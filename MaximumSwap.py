"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: 9973
Output: 9973
Explanation: No swap.

Note:
The given number is in the range [0, 10^8]
"""
class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        pos = [-1]*10
        numStr = str(num)
        for i,c in enumerate(numStr):
            pos[int(c)] = i
        for i,c in enumerate(numStr):
            for j in range(9,int(c),-1):
                if pos[j]>i:
                    k = pos[j]
                    ret = numStr[:i]+numStr[k]+numStr[i+1:k]+numStr[i]+numStr[k+1:]
                    return int(ret)
        return num
