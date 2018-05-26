"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class PascalsTriangle:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        if numRows==0:
            return ret
        ret.append([1])
        if numRows==1:
            return ret
        ret.append([1,1])
        if numRows==2:
            return ret
        pre = ret[-1]
        for _ in range(3,numRows+1):
            temp = [1]
            for i in range(1,len(pre)):
                temp.append(pre[i-1]+pre[i])
            temp.append(1)
            ret.append(temp)
            pre = temp
        return ret
