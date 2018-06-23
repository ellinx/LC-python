"""
According to the Wikipedia's article:
"The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:

1. Could you solve it in-place? Remember that the board needs to be updated at the same time:
    You cannot update some cells first and then use their updated values to update other cells.
2. In this question, we represent the board using a 2D array.
    In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. 
    How would you address these problems?


"""
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # use bit 1 as new state and then remove old start in bit 0
        def nextState(board, i, j):
            liveNeighbor = 0
            dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
            for each in dirs:
                row = i+each[0]
                col = j+each[1]
                if row>=0 and row<len(board) and col>=0 and col<len(board[0]) and (board[row][col]&1)==1:
                    liveNeighbor += 1
            if (board[i][j]&1)==1:
                if liveNeighbor<2:
                    return 0
                elif liveNeighbor<4:
                    return 1
                else:
                    return 0
            else:
                if liveNeighbor==3:
                    return 1
                else:
                    return 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                temp = nextState(board, i, j)
                board[i][j] |= temp<<1
        #print(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] >>= 1
