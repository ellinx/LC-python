"""
We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall,
"@" is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.
We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.
We can't walk over a lock unless we have the corresponding key.

For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of
the English alphabet in the grid.  This means that there is exactly one key for each lock,
and one lock for each key; and also that the letters used to represent the keys and locks
were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.

Example 1:
Input: ["@.a.#","###.#","b.A.B"]
Output: 8

Example 2:
Input: ["@..aA","..B#.","....b"]
Output: 6


Note:
1. 1 <= grid.length <= 30
2. 1 <= grid[0].length <= 30
3. grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
4. The number of keys is in [1, 6].  Each key has a different letter and opens exactly one lock.
"""
class Solution:
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])
        src = None
        allKeys = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='@':
                    src = [i,j]
                elif grid[i][j] in "abcdef":
                    allKeys |= 1<<(ord(grid[i][j])-ord('a'))
        #print(allKeys)
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        q = collections.deque([[src[0], src[1], 0]])
        visited = set()
        visited.add((src[0], src[1], 0))
        move = 0
        while len(q):
            #print(q)
            size = len(q)
            for _ in range(size):
                i,j,state = q.popleft()
                for each in dirs:
                    ni, nj = i+each[0], j+each[1]
                    if ni>=0 and ni<m and nj>=0 and nj<n and grid[ni][nj]!='#':
                        if grid[ni][nj] in "abcdef":
                            nxt = state|(1<<(ord(grid[ni][nj])-ord('a')))
                            if nxt==allKeys:
                                return move+1
                            if (ni,nj,nxt) not in visited:
                                visited.add((ni,nj,nxt))
                                q.append([ni,nj,nxt])
                        elif grid[ni][nj] in "ABCDEF":
                            if state&(1<<(ord(grid[ni][nj])-ord('A')))!=0:
                                if (ni,nj,state) not in visited:
                                    visited.add((ni,nj,state))
                                    q.append([ni,nj,state])
                        else:
                            if (ni,nj,state) not in visited:
                                visited.add((ni,nj,state))
                                q.append([ni,nj,state])
            move += 1
        return -1
