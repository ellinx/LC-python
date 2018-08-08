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
        if start==destination:
            return 0
        m = len(maze)
        n = len(maze[0])
        ret = -1
        dist = dict()
        q = collections.deque()
        dist[tuple(start)] = 0
        q.append([0,start])
        while len(q):
            cur = q.popleft()
            if cur[1]==destination:
                ret = cur[0] if ret==-1 else min(ret,cur[0])
            #print(cur)
            #up
            end = [cur[1][0], cur[1][1]]
            while end[0]>=0 and maze[end[0]][end[1]]==0:
                end[0] -= 1
            end[0] += 1
            #print("up:",end)
            k, val = tuple(end), cur[0]+cur[1][0]-end[0]
            if k not in dist or val<dist[k]:
                dist[k] = val
                q.append([val, end])
            #down
            end = [cur[1][0], cur[1][1]]
            while end[0]<m and maze[end[0]][end[1]]==0:
                end[0] += 1
            end[0] -= 1
            #print("down:",end)
            k, val = tuple(end), cur[0]+end[0]-cur[1][0]
            if k not in dist or val<dist[k]:
                dist[k] = val
                q.append([val, end])
            #left
            end = [cur[1][0], cur[1][1]]
            while end[1]>=0 and maze[end[0]][end[1]]==0:
                end[1] -= 1
            end[1] += 1
            #print("left:",end)
            k, val = tuple(end), cur[0]+cur[1][1]-end[1]
            if k not in dist or val<dist[k]:
                dist[k] = val
                q.append([val, end])
            #right
            end = [cur[1][0], cur[1][1]]
            while end[1]<n and maze[end[0]][end[1]]==0:
                end[1] += 1
            end[1] -= 1
            #print("right:",end)
            k, val = tuple(end), cur[0]+end[1]-cur[1][1]
            if k not in dist or val<dist[k]:
                dist[k] = val
                q.append([val, end])
        return ret
