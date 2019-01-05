"""
You are given a m x n 2D grid initialized with these three possible values.

-1  - A wall or an obstacle.
0   - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF
        as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate.
If it is impossible to reach a gate, it should be filled with INF.

Example:

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        INF = 2**31-1
        m = len(rooms)
        if m==0:
            return
        n = len(rooms[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    q.append([i,j])
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        step = 0
        while len(q):
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for each in dirs:
                    ni = i+each[0]
                    nj = j+each[1]
                    if ni>=0 and ni<m and nj>=0 and nj<n and rooms[ni][nj]==INF:
                        rooms[ni][nj] = step+1
                        q.append([ni,nj])
            step += 1
