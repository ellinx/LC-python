"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

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
        #BFS
        INF = 2147483647
        m = len(rooms)
        if m==0:
            return
        n = len(rooms[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    q.append([i,j])
        level = 0
        while len(q):
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                #up
                if cur[0]>0 and rooms[cur[0]-1][cur[1]]==INF:
                    rooms[cur[0]-1][cur[1]] = level+1
                    q.append([cur[0]-1,cur[1]])
                #down
                if cur[0]<m-1 and rooms[cur[0]+1][cur[1]]==INF:
                    rooms[cur[0]+1][cur[1]] = level+1
                    q.append([cur[0]+1,cur[1]])
                #left
                if cur[1]>0 and rooms[cur[0]][cur[1]-1]==INF:
                    rooms[cur[0]][cur[1]-1] = level+1
                    q.append([cur[0],cur[1]-1])
                #right
                if cur[1]<n-1 and rooms[cur[0]][cur[1]+1]==INF:
                    rooms[cur[0]][cur[1]+1] = level+1
                    q.append([cur[0],cur[1]+1])
            level += 1
