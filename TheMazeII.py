"""
There is a ball in a maze with empty spaces and walls.
The ball can go through empty spaces by rolling up, down, left or right,
but it won't stop rolling until hitting a wall.
When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze,
find the shortest distance for the ball to stop at the destination.
The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded)
 to the destination (included).
If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space.
You may assume that the borders of the maze are all walls.
The start and destination coordinates are represented by row and column indexes.

Example 1

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12
Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1
Explanation: There is no way for the ball to stop at the destination.

Note:

1. There is only one ball and one destination in the maze.
2. Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
3. The given maze does not contain border (like the red rectangle in the example pictures),
    but you could assume the border of the maze are all walls.
4. The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

"""
class Solution:
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        q = collections.deque()
        q.append([0, start])
        dist = dict()
        while len(q):
            step, cur = q.popleft()
            # up
            i, j = cur
            while i>=0 and maze[i][j]==0:
                i -= 1
            i += 1
            if step+cur[0]-i<dist.get((i,j), float('inf')):
                dist[(i,j)] = step+cur[0]-i
                q.append([dist[(i,j)], [i,j]])
            # down
            i, j = cur
            while i<m and maze[i][j]==0:
                i += 1
            i -= 1
            if step+i-cur[0]<dist.get((i,j), float('inf')):
                dist[(i,j)] = step+i-cur[0]
                q.append([dist[(i,j)], [i,j]])
            # left
            i, j = cur
            while j>=0 and maze[i][j]==0:
                j -= 1
            j += 1
            if step+cur[1]-j<dist.get((i,j), float('inf')):
                dist[(i,j)] = step+cur[1]-j
                q.append([dist[(i,j)], [i,j]])
            # right
            i, j = cur
            while j<n and maze[i][j]==0:
                j += 1
            j -= 1
            if step+j-cur[1]<dist.get((i,j), float('inf')):
                dist[(i,j)] = step+j-cur[1]
                q.append([dist[(i,j)], [i,j]])
        return dist.get(tuple(destination), -1)
