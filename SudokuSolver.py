"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

    The given board contain only digits 1-9 and the character '.'.
    You may assume that the given Sudoku puzzle will have a single unique solution.
    The given board size is always 9x9.


"""
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def dfs(board, q):
            if len(q)==0:
                return True
            row, col = q.popleft()
            used = [False]*10
            #check row
            for i in range(len(board[row])):
                if board[row][i]!=".":
                    used[int(board[row][i])] = True
            # check col
            for i in range(len(board)):
                if board[i][col]!=".":
                    used[int(board[i][col])] = True
            # check 3x3
            start = [row//3*3, col//3*3]
            for i in range(3):
                for j in range(3):
                    if board[start[0]+i][start[1]+j]!=".":
                        used[int(board[start[0]+i][start[1]+j])] = True
            # dfs unused numbers
            for i in range(1,10):
                if not used[i]:
                    board[row][col] = str(i)
                    if dfs(board, q):
                        return True
            board[row][col] = "."
            q.appendleft((row,col))
            return False

        q = collections.deque()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    q.append((i,j))
        dfs(board, q)
