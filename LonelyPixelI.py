"""
Given a picture consisting of black and white pixels,
find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W',
which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position
where the same row and same column don't have any other black pixels.

Example:
Input:
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.

Note:
The range of width and height of the input 2D array is [1,500].
"""
class Solution:
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        m = len(picture)
        if m==0:
            return 0
        n = len(picture[0])
        rows = [0]*m
        cols = [0]*n
        for i in range(m):
            for j in range(n):
                if picture[i][j]=='B':
                    rows[i] += 1
                    cols[j] += 1
        ret = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j]=='B' and rows[i]==1 and cols[j]==1:
                    ret += 1
        return ret
