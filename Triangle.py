"""
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.

"""
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle)==0:
            return 0
        cur = triangle[0]
        for i in range(1,len(triangle)):
            nxt = [0]*len(triangle[i])
            for j in range(len(nxt)-1):
                nxt[j] = cur[j]
                if j>0:
                    nxt[j] = min(nxt[j],cur[j-1])
                nxt[j] += triangle[i][j]
            nxt[-1] = cur[-1]+triangle[i][-1]
            #print(nxt)
            cur = nxt
        return min(cur)
