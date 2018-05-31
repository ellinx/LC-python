"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isValid(board, starti, startj):
            count = collections.defaultdict(int)
            for i in range(starti,starti+3):
                for j in range(startj,startj+3):
                    if board[i][j]=='.':
                        continue
                    count[board[i][j]] += 1
                    if count[board[i][j]]>1:
                        return False
            return True

        digits = '123456789'
        # check rows
        for row in range(9):
            count = collections.defaultdict(int)
            for c in board[row]:
                if c=='.':
                    continue
                if c not in digits:
                    return False
                count[c] += 1
                if count[c]>1:
                    return False
        # check cols
        for col in range(9):
            count = collections.defaultdict(int)
            for i in range(9):
                if board[i][col]=='.':
                    continue
                if board[i][col] not in digits:
                    return False
                count[board[i][col]] += 1
                if count[board[i][col]]>1:
                    return False
        # check 3x3
        for i in range(0,7,3):
            for j in range(0,7,3):
                if not isValid(board, i, j):
                    return False
        return True
