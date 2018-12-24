"""
On a 2D plane, we place stones at some integer coordinate points.
Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?


Example 1:
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5

Example 2:
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3

Example 3:
Input: stones = [[0,0]]
Output: 0


Note:

1 <= stones.length <= 1000
0 <= stones[i][j] < 10000
"""
class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        roots = dict()

        def find(x):
            while roots[x]!=x:
                x = roots[x]
            return x

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx!=ry:
                roots[rx] = ry

        for x,y in stones:
            roots.setdefault((x,-1), (x,-1))
            roots.setdefault((-1,y), (-1,y))
            union((x,-1),(-1,y))
        #print(roots)
        return len(stones)-len({find(each) for each in roots})
