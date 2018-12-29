"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

    [1]
   [1,1]
  [1,2,1]
 [1,3,3,1]
[1,4,6,4,1]

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        cur = [1]
        for _ in range(rowIndex):
            nxt = [1]
            for i in range(1,len(cur)):
                nxt.append(cur[i-1]+cur[i])
            nxt.append(1)
            cur = nxt
        return cur
