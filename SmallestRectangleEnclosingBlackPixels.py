"""
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel.
The black pixels are connected, i.e., there is only one black region.
Pixels are connected horizontally and vertically.

Given the location (x, y) of one of the black pixels,
return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Example:

Input:
[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2

Output: 6
"""
class Solution:
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        def dfs(image, x, y, ret):
            image[x][y] = '0'
            ret[0] = min(ret[0], x)
            ret[1] = max(ret[1], x)
            ret[2] = min(ret[2], y)
            ret[3] = max(ret[3], y)
            dirs = [[-1,0],[1,0],[0,-1],[0,1]]
            for each in dirs:
                i = x+each[0]
                j = y+each[1]
                if i>=0 and i<len(image) and j>=0 and j<len(image[0]) and image[i][j]=='1':
                    dfs(image, i, j, ret)

        ret = [x,x,y,y]
        dfs(image, x, y, ret)
        #print(ret)
        return (ret[1]-ret[0]+1)*(ret[3]-ret[2]+1)
