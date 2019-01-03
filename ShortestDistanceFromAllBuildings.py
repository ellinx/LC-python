"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance.
You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.

Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total
             travel distance of 3+3+1=7 is minimal. So return 7.
             
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""
class Solution:
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dist = dict()
        buildings = list()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    dist[(i,j)] = [0,0]
                elif grid[i][j]==1:
                    buildings.append([i,j])
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        for i,j in buildings:
            q = collections.deque([[i,j,0]])
            visited = set()
            while len(q):
                cur = q.popleft()
                for each in dirs:
                    ni = cur[0]+each[0]
                    nj = cur[1]+each[1]
                    if ni>=0 and ni<m and nj>=0 and nj<n and grid[ni][nj]==0 and (ni,nj) not in visited:
                        dist[(ni,nj)][0] += cur[2]+1
                        dist[(ni,nj)][1] += 1
                        visited.add((ni,nj))
                        q.append([ni,nj,cur[2]+1])
        ret = -1
        #print(dist)
        for k in dist:
            if dist[k][1]==len(buildings):
                ret = min(ret, dist[k][0]) if ret!=-1 else dist[k][0]
        return ret
