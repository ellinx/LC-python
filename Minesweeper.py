"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board.
'M' represents an unrevealed mine, 'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines,
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'),
return the board after revealing this position according to the following rules:

1. If a mine ('M') is revealed, then the game is over - change it to 'X'.
2. If an empty square ('E') with no adjacent mines is revealed,
    then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
3. If an empty square ('E') with at least one adjacent mine is revealed,
    then change it to a digit ('1' to '8') representing the number of adjacent mines.
4. Return the board when no more squares will be revealed.

Example 1:

Input:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Note:

1. The range of the input matrix's height and width is [1,50].
2. The click position will only be an unrevealed square ('M' or 'E'),
    which also means the input board contains at least one clickable square.
3. The input board won't be a stage when game is over (some mines have been revealed).
4. For simplicity, not mentioned rules should be ignored in this problem.
    For example, you don't need to reveal all the unrevealed mines when the game is over,
    consider any cases that you will win the game or flag any squares.

"""
class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]] = 'X'
            return board
        m, n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]
        q = collections.deque()
        q.append(click)
        visited[click[0]][click[1]] = True
        dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        while len(q):
            cur = q.popleft()
            adjacent_mine = 0
            adjacent_empty = []
            for each in dirs:
                i = cur[0]+each[0]
                j = cur[1]+each[1]
                if i>=0 and i<m and j>=0 and j<n:
                    if board[i][j]=='M':
                        adjacent_mine += 1
                    if board[i][j]=='E' and not visited[i][j]:
                        adjacent_empty.append([i,j])
            if adjacent_mine>0:
                board[cur[0]][cur[1]] = str(adjacent_mine)
            else:
                board[cur[0]][cur[1]] = 'B'
                for pos in adjacent_empty:
                    q.append(pos)
                    visited[pos[0]][pos[1]] = True
            #print(q)
        return board
