"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

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
        ret = num
        numStr = str(num)
        for i in range(len(numStr)-1):
            maxAfterI = i+1
            for j in range(i+1,len(numStr)):
                if numStr[j]>=numStr[maxAfterI]:
                    maxAfterI = j
            if numStr[i]<numStr[maxAfterI]:
                ret = max(ret, int(numStr[:i]+numStr[maxAfterI]+numStr[i+1:maxAfterI]+numStr[i]+numStr[maxAfterI+1:]))
        return ret
