"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def putQueen(board, row, n, ret):
            if n==row:
                ret.append(list(board))
                return
            for i in range(n):
                if canPutQueen(board, row, i):
                    board[row] = board[row][:i]+'Q'+board[row][i+1:]
                    putQueen(board, row+1, n, ret)
                    board[row] = board[row][:i]+'.'+board[row][i+1:]

        def canPutQueen(board, row, col):
            # check same col
            for i in range(len(board)):
                if board[i][col]=='Q':
                    return False
            # check diag
            i,j = row-1,col+1
            while i>=0 and j<len(board):
                if board[i][j]=='Q':
                    return False
                i -= 1
                j += 1
            i,j = row+1,col-1
            while i<len(board) and j>=0:
                if board[i][j]=='Q':
                    return False
                i += 1
                j -= 1
            i,j = row-1,col-1
            while i>=0 and j>=0:
                if board[i][j]=='Q':
                    return False
                i -= 1
                j -= 1
            i,j = row+1,col+1
            while i<len(board) and j<len(board):
                if board[i][j]=='Q':
                    return False
                i += 1
                j += 1
            return True

        ret = []
        board = ['.'*n for _ in range(n)]
        putQueen(board, 0, n, ret)
        return ret
