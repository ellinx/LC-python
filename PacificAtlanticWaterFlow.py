"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent,
the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        if m==0:
            return []
        n = len(matrix[0])
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        visited = [[0]*n for _ in range(m)]
        # Pacific BFS
        q = collections.deque()
        for i in range(n):
            q.append([0,i])
            visited[0][i] |= 1
        for i in range(1,m):
            q.append([i,0])
            visited[i][0] |= 1
        while len(q):
            cur = q.popleft()
            for each in dirs:
                i = cur[0]+each[0]
                j = cur[1]+each[1]
                if i>=0 and i<m and j>=0 and j<n and visited[i][j]&1==0 and matrix[i][j]>=matrix[cur[0]][cur[1]]:
                    visited[i][j] |= 1
                    q.append([i,j])
        # Atlantic BFS
        for i in range(n):
            q.append([m-1,i])
            visited[m-1][i] |= 2
        for i in range(m-1):
            q.append([i,n-1])
            visited[i][n-1] |= 2
        while len(q):
            cur = q.popleft()
            for each in dirs:
                i = cur[0]+each[0]
                j = cur[1]+each[1]
                if i>=0 and i<m and j>=0 and j<n and visited[i][j]&2==0 and matrix[i][j]>=matrix[cur[0]][cur[1]]:
                    visited[i][j] |= 2
                    q.append([i,j])
        # collect answer
        #print(visited)
        ret = []
        for i in range(m):
            for j in range(n):
                if visited[i][j]&3==3:
                    ret.append([i,j])
        return ret
