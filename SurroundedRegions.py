"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border,
which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def dfs(board, i, j):
            m = len(board)
            n = len(board[0])
            vecs = ((-1,0),(1,0),(0,-1),(0,1))
            board[i][j] = '1'
            for vec in vecs:
                ni = i+vec[0]
                nj = j+vec[1]
                if ni>=0 and ni<m and nj>=0 and nj<n and board[ni][nj]=='O':
                    dfs(board, ni, nj)

        m = len(board)
        if m==0:
            return
        n = len(board[0])
        for i in range(0,n):
            if board[0][i]=='O':
                dfs(board, 0, i)
            if board[m-1][i]=='O':
                dfs(board, m-1, i)
        for i in range(1,m-1):
            if board[i][0]=='O':
                dfs(board, i, 0)
            if board[i][n-1]=='O':
                dfs(board, i, n-1)
        for i in range(0,m):
            for j in range(0,n):
                if board[i][j]=='1':
                    board[i][j] = 'O'
                elif board[i][j]=='O':
                    board[i][j] = 'X'
